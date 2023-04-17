/*==LICENSE==*

CyanWorlds.com Engine - MMOG client, server and tools
Copyright (C) 2011  Cyan Worlds, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Additional permissions under GNU GPL version 3 section 7

If you modify this Program, or any covered work, by linking or
combining it with any of RAD Game Tools Bink SDK, Autodesk 3ds Max SDK,
NVIDIA PhysX SDK, Microsoft DirectX SDK, OpenSSL library, Independent
JPEG Group JPEG library, Microsoft Windows Media SDK, or Apple QuickTime SDK
(or a modified version of those libraries),
containing parts covered by the terms of the Bink SDK EULA, 3ds Max EULA,
PhysX SDK EULA, DirectX SDK EULA, OpenSSL and SSLeay licenses, IJG
JPEG Library README, Windows Media SDK EULA, or QuickTime SDK EULA, the
licensors of this Program grant you additional
permission to convey the resulting work. Corresponding Source for a
non-source form of such a combination shall include the source code for
the parts of OpenSSL and IJG JPEG Library used as well as that of the covered
work.

You can contact Cyan Worlds, Inc. by email legal@cyan.com
 or by snail mail at:
      Cyan Worlds, Inc.
      14617 N Newport Hwy
      Mead, WA   99021

*==LICENSE==*/
///////////////////////////////////////////////////////////////////////////////
//                                                                           //
//  plTextFont Class Functions                                               //
//  Cyan, Inc.                                                               //
//                                                                           //
//// Version History //////////////////////////////////////////////////////////
//                                                                           //
//  2.19.2001 mcn - Created.                                                 //
//                                                                           //
///////////////////////////////////////////////////////////////////////////////

#include "plTextFont.h"

#include "HeadSpin.h"
#include "hsWindows.h"

#include "plDebugText.h"

#include <ft2build.h>
#include FT_FREETYPE_H
#include FT_GLYPH_H

#include <memory>

#if defined(HS_BUILD_FOR_APPLE)
#import <CoreGraphics/CoreGraphics.h>
#import <CoreText/CoreText.h>
#endif

#define DisplayableChar(c) (c >= 0 && c <= 128)

//// Constructor & Destructor /////////////////////////////////////////////////

plTextFont::plTextFont( plPipeline *pipe )
{
    fMaxNumIndices = 1024;
    fInitialized = false;
    fPipe = pipe;
}

plTextFont::~plTextFont()
{
    IUnlink();
}

//// IInitFontTexture /////////////////////////////////////////////////////////

uint16_t  *plTextFont::IInitFontTexture()
{
#ifdef HS_BUILD_FOR_WIN32
    int     nHeight, x, y, c;
    char    myChar[ 2 ] = "x";

    BITMAPINFO  bmi;
    HDC         hDC;
    HFONT       hFont;
    SIZE        size;
    BYTE        bAlpha;

    
    // Figure out our texture size
    if( fSize > 40 )
        fTextureWidth = fTextureHeight = 1024;
    else if( fSize > 20 )
        fTextureWidth = fTextureHeight = 512;
    else
        fTextureWidth = fTextureHeight = 256;

    /// Now create the data block
    uint16_t* data = new uint16_t[fTextureWidth * fTextureHeight]();
    
    hDC = CreateCompatibleDC(nullptr);
    SetMapMode( hDC, MM_TEXT );

    nHeight = -MulDiv( fSize, GetDeviceCaps( hDC, LOGPIXELSY ), 72 );
    fFontHeight = -nHeight;

    FT_Library  library;
    FT_Face     face;
    FT_Error ftError = FT_Init_FreeType(&library);
    hsAssert(ftError == FT_Err_Ok, "FreeType did not initialize");

    hFont = CreateFont( nHeight, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE, DEFAULT_CHARSET, OUT_DEFAULT_PRECIS,
                        CLIP_DEFAULT_PRECIS, ANTIALIASED_QUALITY, VARIABLE_PITCH, fFace );
    hsAssert(hFont != nullptr, "Cannot create Windows font");

    SelectObject( hDC, hFont );
    // Get the font data

    DWORD fontDataSize = GetFontData( hDC, 0, 0, 0, 0 );
    void* fontData = std::malloc( fontDataSize );
    GetFontData(hDC, 0, 0, fontData, fontDataSize);
    ftError = FT_New_Memory_Face(library, (FT_Byte *) fontData, fontDataSize, 0, &face);

    FT_UInt freeTypeResolution = GetDeviceCaps(hDC, LOGPIXELSY);
    ftError = FT_Set_Char_Size(face, 0, fSize * 64, freeTypeResolution, freeTypeResolution);

    // Set text colors
    SetTextColor( hDC, RGB( 255, 255, 255 ) );
    SetBkColor( hDC, 0 );
    SetTextAlign( hDC, TA_TOP );

    fFontHeight = face->size->metrics.height / 64;
    
    data[0] = 0xffff;

    // Loop through characters, drawing them one at a time
    for( c = 32, x = 1, y = 0; c < 127; c++ )
    {
        myChar[ 0 ] = c;
        ftError = FT_Load_Char(face, c, FT_LOAD_RENDER | FT_LOAD_TARGET_MONO | FT_LOAD_MONOCHROME | FT_LOAD_NO_AUTOHINT | FT_LOAD_NO_HINTING );

        FT_GlyphSlot slot = face->glyph;

        FT_Glyph glyph;
        FT_Get_Glyph(slot, &glyph);

        size.cx = slot->metrics.horiAdvance / 64;
        size.cy = face->ascender / 64;

        FT_Bitmap bitmap = slot->bitmap;

        if( (uint32_t)( x + size.cx + 1 ) > fTextureWidth )
        {
            x = 0;
            y += size.cy + 1;
        }
        int offset = size.cy - face->glyph->bitmap_top - ceil( - face->descender / 64 );

        //blit the bitmap into place
        for (int glyphY = bitmap.rows - 1; glyphY >= 0 ; glyphY--) {
            for (int glyphX = 0; glyphX < bitmap.width; glyphX++) {
                //1 bit Bitmap as source
                int pitch = abs(slot->bitmap.pitch);
                unsigned char* row = &slot->bitmap.buffer[pitch * glyphY];
                unsigned char cValue = row[glyphX >> 3];

                uint16_t src = 0;

                if ((cValue & (128 >> (glyphX & 7))) != 0) {
                    src = UINT16_MAX;
                }
                int destY = y + glyphY + offset;
                int destX = glyphX + x + face->glyph->bitmap_left;
                int destIndex = (destY * fTextureWidth) + destX;

                data[(destIndex )] = src;
            }
        }

        fCharInfo[ c ].fW = (uint16_t)size.cx;
        fCharInfo[ c ].fH = (uint16_t)size.cy;
        fCharInfo[ c ].fUVs[ 0 ].fX = (float)x / (float)fTextureWidth;
        fCharInfo[ c ].fUVs[ 0 ].fY = (float)y / (float)fTextureHeight;
        fCharInfo[ c ].fUVs[ 1 ].fX = (float)( x + size.cx ) / (float)fTextureWidth;
        fCharInfo[ c ].fUVs[ 1 ].fY = (float)( y + size.cy ) / (float)fTextureHeight;
        fCharInfo[ c ].fUVs[ 0 ].fZ = fCharInfo[ c ].fUVs[ 1 ].fZ = 0;

        x += size.cx + 1;
    }
    fCharInfo[ 32 ].fUVs[ 1 ].fX = fCharInfo[ 32 ].fUVs[ 0 ].fX;

    // Special case the tab key
    fCharInfo[ '\t' ].fUVs[ 1 ].fX = fCharInfo[ '\t' ].fUVs[ 0 ].fX = fCharInfo[ 32 ].fUVs[ 0 ].fX;
    fCharInfo[ '\t' ].fUVs[ 1 ].fY = fCharInfo[ '\t' ].fUVs[ 0 ].fY = 0;
    fCharInfo[ '\t' ].fUVs[ 0 ].fZ = fCharInfo[ '\t' ].fUVs[ 1 ].fZ = 0;
    fCharInfo[ '\t' ].fW = fCharInfo[ 32 ].fW * 4;
    fCharInfo[ '\t' ].fH = fCharInfo[ 32 ].fH;

    FT_Done_Face(face);
    FT_Done_FreeType(library);

    // Cleanup and return
    DeleteDC( hDC );
    DeleteObject( hFont );

    return data;
#elif defined(HS_BUILD_FOR_APPLE)
    int     nHeight, x, y, c;
    char    myChar[ 2 ] = "x";
    uint16_t  *tBits;

    uint32_t       *bitmapBits;
    uint32_t        bAlpha;

    
    // Figure out our texture size
    if( fSize * 2 > 40 )
        fTextureWidth = fTextureHeight = 1024;
    else if( fSize * 2 > 20 )
        fTextureWidth = fTextureHeight = 512;
    else
        fTextureWidth = fTextureHeight = 256;


    // Create a new DC and bitmap that we can draw characters to
    CGColorSpaceRef colorSpace = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB);
    CGContextRef bitmapContext = CGBitmapContextCreate(nullptr,
                                                fTextureWidth,
                                                fTextureHeight,
                                                8,
                                                4 * fTextureWidth,
                                                colorSpace,
                                                kCGImageAlphaPremultipliedLast);
    CFRelease(colorSpace);
    CGContextSetTextMatrix(bitmapContext, CGAffineTransformMakeScale(1, -1));
    CGContextTranslateCTM(bitmapContext, 0, fTextureHeight);
    CGContextScaleCTM(bitmapContext, 1, -1);
    CGContextScaleCTM(bitmapContext, 2.0, 2.0);
    
    bitmapBits = (uint32_t *)CGBitmapContextGetData(bitmapContext);

    //TEMPORARY: Mac client should vend through better data to make this decision
    nHeight = fSize;
    fFontHeight = (fSize * 144.0f) / 72.0f;

    CFStringRef fontName = CFStringCreateWithCString(nullptr, fFace, kCFStringEncodingUTF8);
    CTFontRef font = CTFontCreateWithName(fontName, nHeight, nullptr);
    hsAssert(font != nullptr, "Cannot create Mac font");
    CFRelease(fontName);

    // Set text colors
    CGFloat color[4] = { 255.0f, 255.0f, 255.0f, 255.0f };
    CGContextSetFillColor(bitmapContext, color);
    CGContextSetShouldAntialias(bitmapContext, false);

    // Loop through characters, drawing them one at a time
    CGRect    r = CGRectMake(0, 0, 10, 10);

    fTextureWidth /= 2;
    fTextureHeight /= 2;
    
    // (Make first character a black dot, for filling rectangles)
    bitmapBits[0] = UINT32_MAX;
    for( c = 32, x = 1, y = 0; c < 127; c++ )
    {
        myChar[ 0 ] = c;
        CGGlyph glpyh;
        CTFontGetGlyphsForCharacters(font, (UniChar *)myChar, &glpyh, 1);
        CGRect rect;
        CTFontGetOpticalBoundsForGlyphs(font, &glpyh, &rect, 1, 0);
        CGSize size = rect.size;

        if( (uint32_t)( x + size.width + 1 ) > fTextureWidth )
        {
            x = 0;
            y += size.height + 1;
        }

        CGPoint position = CGPointMake(x, -y - size.height - rect.origin.y);
        CTFontDrawGlyphs(font, &glpyh, &position, 1, bitmapContext);

        fCharInfo[ c ].fW = (uint16_t)size.width * 2.0f;
        fCharInfo[ c ].fH = (uint16_t)size.height * 2.0f;
        fCharInfo[ c ].fUVs[ 0 ].fX = (float)x / (float)fTextureWidth;
        fCharInfo[ c ].fUVs[ 0 ].fY = (float)y / (float)fTextureHeight;
        fCharInfo[ c ].fUVs[ 1 ].fX = (float)( x + size.width ) / (float)fTextureWidth;
        fCharInfo[ c ].fUVs[ 1 ].fY = (float)( y + size.height ) / (float)fTextureHeight;
        fCharInfo[ c ].fUVs[ 0 ].fZ = fCharInfo[ c ].fUVs[ 1 ].fZ = 0;

        x += ceil(size.width) + 1;
    }
    fCharInfo[ 32 ].fUVs[ 1 ].fX = fCharInfo[ 32 ].fUVs[ 0 ].fX;

    // Special case the tab key
    fCharInfo[ '\t' ].fUVs[ 1 ].fX = fCharInfo[ '\t' ].fUVs[ 0 ].fX = fCharInfo[ 32 ].fUVs[ 0 ].fX;
    fCharInfo[ '\t' ].fUVs[ 1 ].fY = fCharInfo[ '\t' ].fUVs[ 0 ].fY = 0;
    fCharInfo[ '\t' ].fUVs[ 0 ].fZ = fCharInfo[ '\t' ].fUVs[ 1 ].fZ = 0;
    fCharInfo[ '\t' ].fW = fCharInfo[ 32 ].fW * 4;
    fCharInfo[ '\t' ].fH = fCharInfo[ 32 ].fH;
    
    fTextureWidth *= 2;
    fTextureHeight *= 2;

    /// Now create the data block
    uint16_t  *data = new uint16_t[ fTextureWidth * fTextureHeight ];
    tBits = data;
    for( y = 0; y < fTextureHeight; y++ )
    {
        for( x = 0; x < fTextureWidth; x++ )
        {
            bAlpha = (char)( ( bitmapBits[ fTextureWidth * y + x ] & 0xff ) >> 4 );

            if( bitmapBits[ fTextureWidth * y + x ] )
                *tBits = 0xffff;
            else
                *tBits = 0;

            tBits++;
        }
    }

    // Cleanup and return
    CFRelease(font);
    CFRelease(bitmapContext);

    return data;
#else
    return nullptr;
#endif
}

//// Create ///////////////////////////////////////////////////////////////////

void    plTextFont::Create( char *face, uint16_t size )
{
    // Init normal stuff
    strncpy( fFace, face, sizeof( fFace ) );
    fSize = size;
}

//// IInitObjects /////////////////////////////////////////////////////////////

void    plTextFont::IInitObjects()
{
    uint16_t  *data;


    // Create texture
    data = IInitFontTexture();
    hsAssert(data != nullptr, "Cannot create font texture");

    ICreateTexture( data );
    delete [] data;

    // Create state blocks
    IInitStateBlocks();

    fInitialized = true;
}

//// DrawString ///////////////////////////////////////////////////////////////

void    plTextFont::DrawString( const char *string, int sX, int sY, uint32_t hexColor, 
                                uint8_t style, uint32_t rightEdge )
{
    static std::vector<plFontVertex> verts;
    
    int     i, j, width, height, count, thisCount, italOffset;
    float   x = (float)sX;
    char    c, *strPtr;


    if( !fInitialized )
        IInitObjects();

    /// Set up to draw
    italOffset = ( style & plDebugText::kStyleItalic ) ? fSize / 2: 0;
    count = strlen( string );
    strPtr = (char *)string;
    while( count > 0 )
    {
        thisCount = ( count > 64 ) ? 64 : count;
        count -= thisCount;

        // Create an array for our vertices
        verts.resize(thisCount * ((style & plDebugText::kStyleBold) ? 12 : 6));
    
        // Fill them all up now
        for( i = 0; i < thisCount * ( ( style & plDebugText::kStyleBold ) ? 12 : 6 ); i++ )
        {
            verts[ i ].fColor = hexColor;
            verts[ i ].fPoint.fZ = 0;
        }

        for( i = 0, j = 0; i < thisCount; i++, j += 6 )
        {
            c = strPtr[ i ];
            // make sure its a character we will display
            if ( DisplayableChar(c) )
            {
                width = fCharInfo[uint8_t(c)].fW + 1;
                height = fCharInfo[uint8_t(c)].fH + 1;

                if( rightEdge > 0 && x + width + italOffset >= rightEdge )
                {
                    count = 0;
                    thisCount = i;
                    break;
                }

                verts[ j ].fPoint.fX = x + italOffset;
                verts[ j ].fPoint.fY = (float)sY;
                verts[ j ].fUV = fCharInfo[uint8_t(c)].fUVs[ 0 ];

                verts[ j + 1 ].fPoint.fX = x + width + italOffset;
                verts[ j + 1 ].fPoint.fY = (float)sY;
                verts[ j + 1 ].fUV = fCharInfo[uint8_t(c)].fUVs[ 0 ];
                verts[ j + 1 ].fUV.fX = fCharInfo[uint8_t(c)].fUVs[ 1 ].fX;

                verts[ j + 2 ].fPoint.fX = x;
                verts[ j + 2 ].fPoint.fY = (float)sY + height;
                verts[ j + 2 ].fUV = fCharInfo[uint8_t(c)].fUVs[ 0 ];
                verts[ j + 2 ].fUV.fY = fCharInfo[uint8_t(c)].fUVs[ 1 ].fY;

                verts[ j + 3 ].fPoint.fX = x;
                verts[ j + 3 ].fPoint.fY = (float)sY + height;
                verts[ j + 3 ].fUV = fCharInfo[uint8_t(c)].fUVs[ 0 ];
                verts[ j + 3 ].fUV.fY = fCharInfo[uint8_t(c)].fUVs[ 1 ].fY;

                verts[ j + 4 ].fPoint.fX = x + width + italOffset;
                verts[ j + 4 ].fPoint.fY = (float)sY;
                verts[ j + 4 ].fUV = fCharInfo[uint8_t(c)].fUVs[ 0 ];
                verts[ j + 4 ].fUV.fX = fCharInfo[uint8_t(c)].fUVs[ 1 ].fX;

                verts[ j + 5 ].fPoint.fX = x + width;
                verts[ j + 5 ].fPoint.fY = (float)sY + height;
                verts[ j + 5 ].fUV = fCharInfo[uint8_t(c)].fUVs[ 1 ];

                x += width + 1;
            }
        }

        if( thisCount == 0 )
            break;

        if( style & plDebugText::kStyleBold )
        {
            for( i = 0; i < thisCount * 6; i++, j++ )
            {
                verts[ j ] = verts[ i ];
                verts[ j ].fPoint.fX = verts[ j ].fPoint.fX + 1.0f;
            }
        }

        /// TEMPORARY DEBUG ONLY: see if we can catch this stupid random draw bug
#if 0
        for( i = 0; i < thisCount * ( ( style & plDebugText::kStyleBold ) ? 12 : 6 ); i += 3 )
        {
            for( j = 0; j < 3; j++ )
            {
                hsAssert( verts[ i + j ].fPoint.fX >= 0, "Text point out of range" );
                hsAssert( verts[ i + j ].fPoint.fY >= 0, "Text point out of range" );
                hsAssert( verts[ i + j ].fPoint.fX < 1024, "Text point out of range" );
                hsAssert( verts[ i + j ].fPoint.fY < 768, "Text point out of range" );
            }
            int lt = ( verts[ i ].fPoint.fX < verts[ i + 1 ].fPoint.fX ? verts[ i ].fPoint.fX : verts[ i + 1 ].fPoint.fX );
            lt = ( verts[ i + 2 ].fPoint.fX < lt ? verts[ i + 2 ].fPoint.fX : lt );

            int tp = ( verts[ i ].fPoint.fY < verts[ i + 1 ].fPoint.fY ? verts[ i ].fPoint.fY : verts[ i + 1 ].fPoint.fY );
            tp = ( verts[ i + 2 ].fPoint.fY < tp ? verts[ i + 2 ].fPoint.fY : tp );

            int rt = ( verts[ i ].fPoint.fX > verts[ i + 1 ].fPoint.fX ? verts[ i ].fPoint.fX : verts[ i + 1 ].fPoint.fX );
            rt = ( verts[ i + 2 ].fPoint.fX > rt ? verts[ i + 2 ].fPoint.fX : rt );

            int bt = ( verts[ i ].fPoint.fY > verts[ i + 1 ].fPoint.fY ? verts[ i ].fPoint.fY : verts[ i + 1 ].fPoint.fY );
            bt = ( verts[ i + 2 ].fPoint.fY > bt ? verts[ i + 2 ].fPoint.fY : bt );

            hsAssert( rt - lt < 32, "Text character too big" );
            hsAssert( bt - tp < 32, "Text character too big" );
        }
#endif
        /// TEMPORARY DEBUG ONLY: see if we can catch this stupid random draw bug

        
        /// Draw a set of tris now
        IDrawPrimitive(thisCount * ((style & plDebugText::kStyleBold) ? 4 : 2), verts.data());

        strPtr += thisCount;
    }

    /// All done!
}

//// CalcStringWidth //////////////////////////////////////////////////////////

uint32_t  plTextFont::CalcStringWidth( const char *string )
{
    int     i, width = 0;


    if( !fInitialized )
        IInitObjects();
    
    for( i = 0; i < strlen( string ); i++ )
    {
        // make sure its a character we will display
        if ( DisplayableChar(string[i]) )
            width += fCharInfo[uint8_t(string[i])].fW + 2;
    }

    return width;
}

//// DrawRect /////////////////////////////////////////////////////////////////
//  TEMPORARY function to draw a flat-shaded 2D rectangle to the screen. Used
//  to create a background for our console; will be obliterated once we figure
//  a better way to do so.

void    plTextFont::DrawRect( int left, int top, int right, int bottom, uint32_t hexColor )
{
    static std::vector<plFontVertex>   verts;
    int                             i;


    if( !fInitialized )
        IInitObjects();

    /// Draw!
    verts.resize(6);
    for( i = 0; i < 6; i++ )
    {
        verts[ i ].fColor = hexColor;
        verts[ i ].fPoint.fZ = 0;
        verts[ i ].fUV.fX = verts[ i ].fUV.fY = 0;
    }

    verts[ 0 ].fPoint.fX = verts[ 2 ].fPoint.fX = verts[ 3 ].fPoint.fX = (float)left;
    verts[ 1 ].fPoint.fX = verts[ 4 ].fPoint.fX = verts[ 5 ].fPoint.fX = (float)right;
    verts[ 0 ].fPoint.fY = verts[ 1 ].fPoint.fY = verts[ 4 ].fPoint.fY = (float)top;
    verts[ 2 ].fPoint.fY = verts[ 3 ].fPoint.fY = verts[ 5 ].fPoint.fY = (float)bottom;

    // omg I had this at 6...just slap the dunce cap on me...-mcn
    IDrawPrimitive(2, verts.data());

    /// All done!
}

//// Draw3DBorder /////////////////////////////////////////////////////////////
//  Draws a 3d border, upper-left with the first color, lower-right with the
//  second. I just LOOOOVE temporary functions :)
//  Note: this way sucks. Live with it.

void    plTextFont::Draw3DBorder( int left, int top, int right, int bottom, uint32_t hexColor1, uint32_t hexColor2 )
{
    static std::vector<plFontVertex>   verts;
    int                             i;


    if( !fInitialized )
        IInitObjects();

    /// Draw!
    verts.resize(8);
    for( i = 0; i < 8; i++ )
    {
        verts[ i ].fColor = hexColor1;
        verts[ i ].fPoint.fZ = 0;
        verts[ i ].fUV.fX = verts[ i ].fUV.fY = 0;
    }

    verts[ 1 ].fPoint.fX = verts[ 2 ].fPoint.fX = verts[ 3 ].fPoint.fX = verts[ 4 ].fPoint.fX = (float)left;
    verts[ 0 ].fPoint.fX = verts[ 5 ].fPoint.fX = verts[ 6 ].fPoint.fX = verts[ 7 ].fPoint.fX = (float)right;

    verts[ 0 ].fPoint.fY = verts[ 1 ].fPoint.fY = verts[ 2 ].fPoint.fY = verts[ 7 ].fPoint.fY = (float)top;
    verts[ 3 ].fPoint.fY = verts[ 4 ].fPoint.fY = verts[ 5 ].fPoint.fY = verts[ 6 ].fPoint.fY = (float)bottom;

    for( i = 4; i < 8; i++ )
        verts[ i ].fColor = hexColor2;

    IDrawLines(4, verts.data());

    /// All done!
}


