add_definitions(-D_LIB)

add_subdirectory(pfAnimation)
add_subdirectory(pfAudio)
add_subdirectory(pfCCR)
add_subdirectory(pfCamera)
add_subdirectory(pfCharacter)
add_subdirectory(pfConditional)
add_subdirectory(pfConsole)
add_subdirectory(pfConsoleCore)
if(WIN32)
    add_subdirectory(pfCrashHandler)
endif()
add_subdirectory(pfGameGUIMgr)
add_subdirectory(pfGameScoreMgr)
add_subdirectory(pfJournalBook)
add_subdirectory(pfLocalizationMgr)
add_subdirectory(pfMessage)
add_subdirectory(pfMoviePlayer)
add_subdirectory(pfPasswordStore)
add_subdirectory(pfPatcher)
add_subdirectory(pfPython)
add_subdirectory(pfSurface)
