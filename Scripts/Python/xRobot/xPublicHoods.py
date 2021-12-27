from Plasma import *

#=====================================
#   voir nxusBookMachine.py
#=====================================

kCategoryCity = 1
kCategoryPrivate = 2
kCategoryPublic = 3
kCategoryPersonal = 4


# hood sorting vars
kSortNone = 0
kSortNameAsc = 1
kSortNameDesc = 2
kSortPopAsc = 3
kSortPopDesc = 4

##controls for hood sorting var
#kSortControlId = {
#    kSortNameAsc : kIDNameAscArrow,
#    kSortNameDesc : kIDNameDescArrow,
#    kSortPopAsc : kIDPopAscArrow,
#    kSortPopDesc : kIDPopDescArrow
#}

class AgeInstance():
    def __init__(self, ageData):
        self.ageInfo = ageData[0]
        self.population = ageData[1]
        self.owners = ageData[2]

class AgeData():
    def __init__(self, ageFilename, defaultMaxPop, linkVisible):
        self.ageFilename = ageFilename
        self.maxPop = defaultMaxPop
        self.linkVisible = linkVisible
        self.instances = list()

class PublicAges():
    def __init__(self):
        self.publicHoods = list()
        self.publicAges = {
            'city' : AgeData(ageFilename = 'city', defaultMaxPop = 20, linkVisible = 1),
            'GreatTreePub' : AgeData(ageFilename = 'GreatTreePub', defaultMaxPop = 100, linkVisible = 0),
            'guildPub' : AgeData(ageFilename = '', defaultMaxPop = 100, linkVisible = 0),
            'Neighborhood02' : AgeData(ageFilename = 'Neighborhood02', defaultMaxPop = 100, linkVisible = 0),
            'Kveer' : AgeData(ageFilename = 'Kveer', defaultMaxPop = 100, linkVisible = 0),
            }

        self.categoryLinksList = {
            kCategoryCity : list(), #city links
            kCategoryPrivate : list(), #private
            kCategoryPublic : list(), #public
            kCategoryPersonal : list() #personal
        }

    def gotPublicAgeList(self, ages):
        if not ages:
            PtDebugPrint("nxusBookMachine.gotPublicAgeList() - got an empty list, which we assume are hoods, clearing hood list")
            self.publicHoods = list()
            #self.IUpdateLinks(kCategoryPublic)
            self.IUpdatePublicLinksList()
            return

        hoods = list()
        #tempInstances = dict()

        for age in ages:
            ageFilename = age[0].getAgeFilename()
            if ageFilename == "Neighborhood":
                # if the current population and number of owners is zero then don't display it
                #looks like it doesn't work (at least on Dirtsand)
                if age[2] != 0 or age[1] != 0:
                    hoods.append(AgeInstance(age))
            #else:
            #    PtDebugPrint("nxusBookMachine.gotPublicAgeList() - got the list of %s instances" % ageFilename)
            #    try:
            #        instances = tempInstances[ageFilename]
            #    except KeyError:
            #        instances = list()
            #        tempInstances[ageFilename] = instances
            #
            #    instances.append(AgeInstance(age))

        #if tempInstances:
        #    for (ageFilename, instances) in tempInstances.iteritems():
        #        try:
        #            self.publicAges[ageFilename].instances = sorted(instances, key = lambda entry : entry.ageInfo.getAgeSequenceNumber())
        #        except KeyError:
        #            PtDebugPrint("nxusBookMachine.gotPublicAgeList(): got age '%s', that wasn't expected" % ageFilename)
        #    #self.IUpdateLinks(kCategoryCity)

        if hoods:
            self.publicHoods = hoods
            #self.IUpdateLinks(kCategoryPublic)
            self.IUpdatePublicLinksList()

    def ISortPublicHoods(self, hoods, hoodSort = kSortNone):
        # if the language is not English, French, or German, we assume it is English and treat it as such
        hoodsToSort = list()
        for hood in hoods:
            hoodLanguage = hood.ageInfo.getAgeLanguage()
            allowLanguage = self.showHoodLanguages.get(hoodLanguage, True)
            if allowLanguage:
                hoodsToSort.append(hood)

        if hoodSort == kSortNone:
            return hoodsToSort

        reverse = (hoodSort in (kSortNameDesc, kSortPopDesc))
        if hoodSort in (kSortNameAsc, kSortNameDesc):
            return sorted(hoodsToSort, key = lambda hood: hood.ageInfo.getDisplayName(), reverse = reverse)
        else:
            return sorted(hoodsToSort, key = lambda hood: hood.population, reverse = reverse)

    def IUpdatePublicLinksList(self):
        sortedHoods = self.ISortPublicHoods(self.publicHoods, self.publicHoodSort)

        hoodLinks = list()
        for hood in sortedHoods:
            displayName = hood.ageInfo.getDisplayName()
            stringLinkInfo = str(hood.population) #TODO: i10n
            description = hood.ageInfo.getAgeDescription()

            newEntry = LinkListEntry(displayName, stringLinkInfo, description)
            newEntry.setLinkStruct(hood.ageInfo) #create link to instance, use default spawnPoint
            hoodLinks.append(newEntry)

        self.categoryLinksList[kCategoryPublic] = hoodLinks

    #def IUpdateLinks(self, categoryId = None):
    #    if not PtIsDialogLoaded(kNexusDialogName):
    #       PtDebugPrint("nxusBookMachine.IUpdateLinks: called without loaded dialog")
    #       return
    #
    #    #return, if we update list, that is currently not displayed (list will be updated on display)
    #    if categoryId is not None and categoryId != self.idCategorySelected:
    #       return
    #
    #    if self.idCategorySelected == kCategoryCity: # city links
    #       self.IUpdateCityLinksList()
    #    elif self.idCategorySelected == kCategoryPrivate: # private links
    #       self.IUpdatePrivateLinksList()
    #    elif self.idCategorySelected == kCategoryPublic: # public links
    #       self.IUpdatePublicLinksList()
    #    else:
    #       self.IUpdatePersonalLinksList()
    #
    #    #assume that list have changed - clear it
    #    self.IClearEntryList()
    #    self.IUpdateGUILinkList()

    def GetPublicAgeList(self):
        #for ageFilename in self.publicAges.keys():
        #    PtGetPublicAgeList(ageFilename, self)
        PtGetPublicAgeList('Neighborhood', self)

#