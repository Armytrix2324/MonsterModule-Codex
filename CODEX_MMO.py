
#Monster Module - Creature Variables
m_listkey = ["CR" , "Type" , "Subtype" , "Book"] #These were originally created for a template when creating variables
l_listkey = ["anywhere" , "battlefields" , "cave" , "coastal" , "deserts and plains" , "demon army" , "devil army" , "dungeons" , "edge of civilisation" , "elemental plains" , "forest" , "grassland" , "hills" , "jungle" , "labratories" , "mountains" , "rivers and lakes" , "ruins" , "swamps" , "tundra" , "urban" , "underdark" , "underground" , "underwater"]
fakekey = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] #When I first made this program, this fakekey identified the variables above. It's a relic
listkey = [m_listkey , l_listkey]
location = "null"


mmo = "Monster Module" #In the original I wrote program, there were other books, but I cant be bothered editing their variables too

mmo3a = "Aarakocra Captain - CR 3, Humanoid, Aarakocra, Monster Module p3\n" #What is ultimately printed when filtered.
m_mmo3a = ['CR 3', 'Humanoid', 'Aarakocra', 'Monster module'] #Keeps the main information used for the filter
l_mmo3a = ["Anywhere" ,"Battlefields" ,"Hills","Mountains","Urban"] #Location filter
k_mmo3a = [l_mmo3a, m_mmo3a, mmo3a] #Lists the above lists, this acts as a key

mmo3b = "Aarakocra Sharpshooter - CR 1/2, Humanoid, Aarakocra, Monster Module p3\n" 
m_mmo3b = ['CR 1/2', 'Humanoid', 'Aarakocra', 'Monster module']
l_mmo3b = ['Anywhere' ,"Battlefields" ,"Hills","Mountains","Urban"]
k_mmo3b = [l_mmo3b, m_mmo3b, mmo3b]

mmo4 = "Aarakocra Priest of Aedrie - CR 8, Humanoid, Aarakocra, Monster Module p4\n" 
m_mmo4 = ['CR 8', 'Humanoid', 'Aarakocra', 'Monster module']
l_mmo4 = ['Anywhere' ,"Battlefields" ,"Hills","Mountains","Urban"]
k_mmo4 = [l_mmo4, m_mmo4, mmo4]

mmo5 = "Aboleth Soverign - CR 16, Abberation, Aboleth, Monster Module p5\n" 
m_mmo5 = ['CR 16', 'Abberation', 'Aboleth', 'Monster module']
l_mmo5 = ["Coastal","Underwater"]
k_mmo5 = [l_mmo5, m_mmo5, mmo5]

mmo6 = "Young Aboleth - CR 5, Abberation, Aboleth, Monster Module p6\n" 
m_mmo6 = ['CR 5', 'Abberation', 'Aboleth', 'Monster module']
l_mmo6 = ["Coastal","Underwater"]
k_mmo6 = [l_mmo6, m_mmo6, mmo6]

mmo7 = "Adlet - CR 1/2, Humanoid, Monster Module p7\n" 
m_mmo7 = ['CR 1/2', 'Humanoid', 'Null', 'Monster module']
l_mmo7 = ["Anywhere","Cave","Deserts and Plains", "Forest", "Grassland","Hills","Jungles","Ruins","Swamps","Tundra"]
k_mmo7 = [l_mmo7, m_mmo7, mmo7]

mmo8 = "Ahklut - CR 12, Monstrosity, Shapeshifter, Monster Module p8\n" 
m_mmo8 = ['CR 12', 'Monstrosity', 'Shapeshifter', 'Monster module']
l_mmo8 = ["Rivers and lakes","Coastal","Underwater"]
k_mmo8 = [l_mmo8, m_mmo8, mmo8]

mmo9 = "Agathion - CR 4, Celestial, Angel, Monster Module p9\n" 
m_mmo9 = ['CR 4', 'Celestial', 'Angel', 'Monster module']
l_mmo9 = ["Anywhere","Divine Realms"]
k_mmo9 = [l_mmo9, m_mmo9, mmo9]

mmo10 = "Valkyrie - CR 8, Celestial, Angel, Monster Module p10\n" 
m_mmo10 = ['CR 8', 'Celestial', 'Angel', 'Monster module']
l_mmo10 = ["Anywhere","Battlefields","Divine Realms"]
k_mmo10 = [l_mmo10, m_mmo10, mmo10]

mmo11a = "Animator's Staff - CR 3, Construct, Animated Object, Monster Module p11\n" 
m_mmo11a = ['CR 2', 'Construct', 'Animated object', 'Monster module']
l_mmo11a = ["Dungeons","Laboratories","Ruins"]
k_mmo11a = [l_mmo11a, m_mmo11a, mmo11a]

mmo11b = "Animator's Wand - CR 1/2, Construct, Animated Object, Monster Module p11\n" 
m_mmo11b = ['CR 1/2', 'Construct', 'Animated object', 'Monster module']
l_mmo11b = ["Dungeons","Laboratories","Ruins"]
k_mmo11b = [l_mmo11b, m_mmo11b, mmo11b]

mmo12a = "Flying Caltrop - CR 1/8, Construct, Animated Object, Monster Module 12\n" 
m_mmo12a = ['CR 1/8', 'Construct', 'Animated object', 'Monster module']
l_mmo12a = ["Dungeons","Laboratories","Ruins"]
k_mmo12a = [l_mmo12a, m_mmo12a, mmo12a]

mmo12b = "Flying Shield - CR 1/2, Construct, Animated Object, Monster Module p12\n" 
m_mmo12b = ['CR 1/2', 'Construct', 'Animated object', 'Monster module']
l_mmo12b = ["Dungeons","Laboratories","Ruins"]
k_mmo12b = [l_mmo12b, m_mmo12b, mmo12b]

mmo13a = "Sack of Smother - CR 1, Construct, Animated Object, Monster Module p13\n" 
m_mmo13a = ['CR 1', 'Construct', 'Animated object', 'Monster module']
l_mmo13a = ["Dungeons","Laboratories","Ruins"]
k_mmo13a = [l_mmo13a, m_mmo13a, mmo13a]

mmo13b = "Swarm of Flying Caltrop - CR 1/2, Construct, Animated Object, Monster Module p13\n" 
m_mmo13b = ['CR 1/2', 'Construct', 'Animated object', 'Monster module']
l_mmo13b = ["Dungeons","Laboratories","Ruins"]
k_mmo13b = [l_mmo13b, m_mmo13b, mmo13b]

mmo13c = "Swarm of Ball Bearings - CR 1, Construct, Animated Object, Monster Module p13\n" 
m_mmo13c = ['CR 1', 'Construct', 'Animated object', 'Monster module']
l_mmo13c = ["Dungeons","Laboratories","Ruins"]
k_mmo13c = [l_mmo13c, m_mmo13c, mmo13c]

mmo14 = "Jungle Ankheg - CR 5, Monstrosity, Ankheg, Monster Module p14\n" 
m_mmo14 = ['CR 5', 'Monstrosity', 'Ankheg', 'Monster module']
l_mmo14 = ["Anywhere","Jungle","Underdark","Underground","Caves","Forest"]
k_mmo14 = [l_mmo14, m_mmo14, mmo14]

mmo15a = "Azer Artisan - CR 3, Elemental, Azer, Monster Module p15\n" 
m_mmo15a = ['CR 3', 'Elemental', 'Azer', 'Monster module']
l_mmo15a = ["Urban","Elemental Plains"]
k_mmo15a = [l_mmo15a, m_mmo15a, mmo15a]

mmo15b = "Azer Lord - CR 6, Humanoid, Azer, Monster Module p15\n"
m_mmo15b = ['CR 6', 'Elemental', 'Azer', 'Monster module']
l_mmo15b = ["Urban","Elemental Plains"]
k_mmo15b = [l_mmo15b, m_mmo15b, mmo15b]

mmo16 = "Baku - CR 9, Fey, Monster Module p16\n" 
m_mmo16 = ['CR 9', 'Fey', 'Null', 'Monster module']
l_mmo16 = ["Urban","Edge of Civilisation","Forests","Caves",]
k_mmo16 = [l_mmo16, m_mmo16, mmo16]

mmo17 = "Bewailer - CR 7, Undead, Banshee, Monster Module p17\n"
m_mmo17 = ['CR 7', 'Undead', 'Banshee', 'Monster module']
l_mmo17 = ["Anywhere","Dungeons","Urban","Forests"]
k_mmo17 = [l_mmo17, m_mmo17, mmo17]

mmo18 = "Greater Basilisk - CR 10, Monstrosity, Basilisk, Monster Module p18\n"
m_mmo18 = ['CR 10', 'Monstrosity', 'Basilisk', 'Monster module']
l_mmo18 = ["Anywhere","Jungle","Forest","Coastal","Caves"]
k_mmo18 = [l_mmo18, m_mmo18, mmo18]

mmo19 = "Marine Basilisk - CR 4, Monstrosity, Basilisk, Monster Module p19\n"
m_mmo19 = ['CR 4', 'Monstrosity', 'Basilisk', 'Monster module']
l_mmo19 = ["Rivers and lakes","Coastal","Underwater"]
k_mmo19 = [l_mmo19, m_mmo19, mmo19]

mmo20 = "Plated Behir - CR 15, Monstrosity, Behir, Monster Module p20\n" 
m_mmo20 = ['CR 4', 'Monstrosity', 'Behir', 'Monster module']
l_mmo20 = ["Anywhere","Jungle","Forest","Caves"]
k_mmo20 = [l_mmo20, m_mmo20, mmo20]

mmo21 = "Eye Of The Deep - CR 5, Aberration, Beholder, Monster Module p21\n"
m_mmo21 = ['CR 5', 'Aberration', 'Beholder', 'Monster module']
l_mmo21 = ["Coastal","Underwater","Caves"]
k_mmo21 = [l_mmo21, m_mmo21, mmo21]

mmo22 = "Bramble Blight - CR 1, Plant, Blight, Monster Module p22\n" 
m_mmo22 = ['CR 1', 'Plant', 'Blight', 'Monster module']
l_mmo22 = ["Forest","Jungles"]
k_mmo22 = [l_mmo22, m_mmo22, mmo22]

mmo23a = "Branch Blight - CR 3, Plant, Blight, Monster Module p23\n" 
m_mmo23a = ['CR 3', 'Plant', 'Blight', 'Monster module']
l_mmo23a = ["Forest","Jungles"]
k_mmo23a = [l_mmo23a, m_mmo23a, mmo23a]

mmo23b = "Wood Blight - CR 1/2, Plant, Blight, Monster Module p23\n" 
m_mmo23b = ['CR 1/2', 'Plant', 'blight', 'monster module']
l_mmo23b = ["Forest","Jungles"]
k_mmo23b = [l_mmo23b, m_mmo23b, mmo23b]

mmo24a = "Bugbear Assassin - CR 6, Humanoid, Bugbear, Monster Module p24\n" 
m_mmo24a = ['CR 6', 'Humanoid', 'bugbear', 'monster module']
l_mmo24a = ["Anywhere","Urban","Forest","Jungles","Battlefields","Edge of Civilisation","Caves","Dungeons"]
k_mmo24a = [l_mmo24a, m_mmo24a, mmo24a]

mmo24b = "Bugbear Champion - CR 4, Humanoid, Bugbear, Monster Module p24\n"
m_mmo24b = ['CR 4', 'Humanoid', 'bugbear', 'monster module']
l_mmo24b = ["Anywhere","Urban","Forest","Jungles","Battlefields","Edge of Civilisation","Caves","Dungeons"]
k_mmo24b = [l_mmo24b, m_mmo24b, mmo24b]

mmo25 = "Bullywug Shaman - CR 3, Humanoid, Bullywug, Monster Module p25\n" 
m_mmo25 = ['CR 3', 'Humanoid', 'bullywug', 'monster module']
l_mmo25 = ["Anywhere","Forest","Jungles","Battlefields","Edge of Civilisation"]
k_mmo25 = [l_mmo25, m_mmo25, mmo25]

mmo26a = "Bullwug Chief - CR 3, Humanoid, Bullywug, Monster Module p26\n" 
m_mmo26a = ['CR 3', 'Humanoid', 'bullywug', 'monster module']
l_mmo26a = ["Anywhere","Forest","Jungles","Battlefields","Edge of Civilisation"]
k_mmo26a = [l_mmo26a, m_mmo26a, mmo26a]

mmo26b = "Bullwug Hunter - CR 1/2, Humanoid, Bullywug, Monster Module p26\n"
m_mmo26b = ['CR 1/2', 'Humanoid', 'bullywug', 'monster module']
l_mmo26b = ["Anywhere","Forest","Jungles","Battlefields","Edge of Civilisation"]
k_mmo26b = [l_mmo26b, m_mmo26b, mmo26b]

mmo27 = "Alu-fiend - CR 4, Fiend, Cambion, Monster Module p27\n" 
m_mmo27 = ['CR 4', 'Fiend', 'cambion', 'monster module']
l_mmo27 = ["Anywhere","Devil Army","Demon Army","Edge of civilisation", "Urban","Dungeons"]
k_mmo27 = [l_mmo27, m_mmo27, mmo27]

mmo28 = "Spawn of Graz'zt - CR 10, Fiend, Cambion, Monster Module p28\n" 
m_mmo28 = ['CR 10', 'Fiend', 'cambion', 'monster module']
l_mmo28 = ["Anywhere","Demon Army","Edge of civilisation", "Urban","Dungeons"]
k_mmo28 = [l_mmo28, m_mmo28, mmo28]

mmo29 = "Spawn of Orcus - CR 15, Fiend, Cambion, Monster Module p29\n" 
m_mmo29 = ['CR 15', 'Fiend', 'cambion', 'monster module']
l_mmo29 = ["Anywhere","Demon Army","Edge of civilisation", "Urban","Dungeons"]
k_mmo29 = [l_mmo29, m_mmo29, mmo29]

mmo30 = "Tangle Crawler - CR 6, Monstrosity, Carrion Crawler, Monster Module p30\n" 
m_mmo30 = ['CR 6', 'Monstrosity', 'carrion crawler', 'monster module']
l_mmo30 = ["Anywhere","Jungle","Underdark","Underground","Caves","Forest"]
k_mmo30 = [l_mmo30, m_mmo30, mmo30]

mmo31 = "Centaur Knight - CR 8, Humanoid, Centuar, Monster Module p31\n"
m_mmo31 = ['CR 8', 'Humanoid', 'centaur', 'monster module']
l_mmo31 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest"]
k_mmo31 = [l_mmo31, m_mmo31, mmo31]

mmo32 = "Centaur Marksman - CR 4, Humanoid, Centuar, Monster Module p32\n" 
m_mmo32 = ['CR 4', 'Humanoid', 'centaur', 'monster module']
l_mmo32 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest"]
k_mmo32 = [l_mmo32, m_mmo32, mmo32]

mmo33a = "Centaur Spritcaller - CR 5, Humanoid, Centuar, Monster Module p33\n" 
m_mmo33a = ['CR 5', 'Humanoid', 'centaur', 'monster module']
l_mmo33a = ["Anywhere","Deserts and plains","Grassland","Hills","Forest"]
k_mmo33a = [l_mmo33a, m_mmo33a, mmo33a]

mmo33b = "Centaur Wildling - CR 6, Humanoid, Centuar, Monster Module p33\n" 
m_mmo33b = ['CR 6', 'Humanoid', 'centaur', 'monster module']
l_mmo33b = ["Anywhere","Deserts and plains","Grassland","Hills","Forest"]
k_mmo33b = [l_mmo33b, m_mmo33b, mmo33b]

mmo34 = "Cerynitis - CR 14, Celestial, Monster Module p34\n" 
m_mmo34 = ['CR 6', 'Celestial', 'null', 'monster module']
l_mmo34 =  ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Divine Realms"]
k_mmo34 = [l_mmo34, m_mmo34, mmo34]

mmo35 = "Astral Chimaera - CR 10, Monstrosity, Chimera, Monster Module p35\n" 
m_mmo35 = ['CR 10', 'Monstrosity', 'chimera', 'monster module']
l_mmo35 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo35 = [l_mmo35, m_mmo35, mmo35]

mmo36 = "Demimaera - CR 4, Monstrosity, Chimera, Monster Module p36\n"
m_mmo36 = ['CR 4', 'Monstrosity', 'chimera', 'monster module']
l_mmo36 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo36 = [l_mmo36, m_mmo36, mmo36]

mmo37 = "Maeragorgon - CR 16, Fiend, Chimera, Monster Module p37\n"
m_mmo37 = ['CR 16', 'Fiend', 'chimera', 'monster module']
l_mmo37 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo37 = [l_mmo37, m_mmo37, mmo37]

mmo38 = "Chupacabra - CR 1, Monstrosity, Monster Module p38\n"
m_mmo38 = ['CR 1', 'Monstrosity', 'null', 'monster module']
l_mmo38 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo38 = [l_mmo38, m_mmo38, mmo38]

mmo39 = "Brass Spider - CR 6, Construct, Clockwork, Monster Module p39\n"
m_mmo39 = ['CR 6', 'Construct', 'clockwork', 'monster module']
l_mmo39 = ["Dungeons","Laboratories","Ruins"]
k_mmo39 = [l_mmo39, m_mmo39, mmo39]

mmo40 = "Electrum Drake - CR 2, Construct, Clockwork, Monster Module p40\n"
m_mmo40 = ['CR 2', 'Construct', 'clockwork', 'monster module']
l_mmo40 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo40 = [l_mmo40, m_mmo40, mmo40]

mmo41 = "Greater Cockatrice - CR 7, Monstrosity, Cockatrice, Monster Module p41\n" 
m_mmo41 = ['CR 2', 'Monstrosity', 'cockatrice', 'monster module']
l_mmo41 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo41 = [l_mmo41, m_mmo41, mmo41]

mmo42 = "Fallen Couatl - CR 4, Celestial, Couatl, Monster Module p42\n" 
m_mmo42 = ['CR 4', 'Celestial', 'couatl', 'monster module']
l_mmo42 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo42 = [l_mmo42, m_mmo42, mmo42]

mmo43 = "Quetzalcouatl - CR 14, Celestial, Couatl, Monster Module p43\n"
m_mmo43 = ['CR 14', 'Celestial', 'couatl', 'monster module']
l_mmo43 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo43 = [l_mmo43, m_mmo43, mmo43]

mmo44 = "Crysmal - CR 3, Elemental, Monster Module p44\n"
m_mmo44 = ['CR 3', 'Elemental', 'null', 'monster module']
l_mmo44 = ["Anywhere","Deserts and plains","Elemental plains","Grassland","Hills","Forest","Mountains"]
k_mmo44 = [l_mmo44, m_mmo44, mmo44]

mmo45 = "Half-Cyclops - CR 2, Giant, Cyclops, Monster Module p45\n" 
m_mmo45 = ['CR 2', 'Celestial', 'couatl', 'monster module']
l_mmo45 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo45 = [l_mmo45, m_mmo45, mmo45]

mmo46 = "Infernal Cyclops - CR 15, Giant, Cyclops, Monster Module p46\n" 
m_mmo46 = ['CR 14', 'Celestial', 'couatl', 'monster module']
l_mmo46 = ["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains","Dungeons"]
k_mmo46 = [l_mmo46, m_mmo46, mmo46]

mmo47 =  "Primal Cyclops - CR 8, Giant, Cyclops, Monster Module p47\n"
m_mmo47 = ['CR 8', 'Celestial', 'couatl', 'monster module']
l_mmo47 =["Anywhere","Deserts and plains","Grassland","Hills","Forest","Mountains"]
k_mmo47 = [l_mmo47, m_mmo47, mmo47]

#Sortlist was originally used to record the amount of creatures in mmolist, but is now used as part of the algorithm to sort, since sublist doesnt work the way I need this to/
sortlist = [    1 ,      2 ,      3,    4  ,    5  ,    6  ,    7  ,    8  ,   9    ,     10  ,   11    ,    12   ,     13  ,    14   ,   15    ,       16,     17 ,   23    ,      24 ,     25 ,      26,    27  ,     28 ,    29  ,   30   ,      31,     32 ,     33   ,      34 ,     35  ,      36,     37  ,     38  ,   39   ,   40   ,      41,     42 ,     43 ,      44 ,     45 ,      46 ,    47  ,     48 ,      49,       47,    48  ,    49  ,    50  ,   51   ,     52 ,    53  ,    54  ,  54    ,   55   ,  56    ]
mmolist = [k_mmo3a, k_mmo3b, k_mmo4, k_mmo5, k_mmo6, k_mmo7, k_mmo8, k_mmo9, k_mmo10, k_mmo11a, k_mmo11b, k_mmo12a, k_mmo12b, k_mmo13a, k_mmo13b, k_mmo13c, k_mmo14, k_mmo15a, k_mmo15b, k_mmo16, k_mmo17, k_mmo18, k_mmo19, k_mmo20, k_mmo21, k_mmo22, k_mmo23a, k_mmo23b, k_mmo24a, k_mmo24b, k_mmo25, k_mmo26a, k_mmo26b, k_mmo27, k_mmo28, k_mmo29, k_mmo30, k_mmo31, k_mmo32, k_mmo33a, k_mmo33b, k_mmo34, k_mmo35, k_mmo36, k_mmo37, k_mmo38, k_mmo39, k_mmo40, k_mmo41, k_mmo42, k_mmo43, k_mmo44, k_mmo45, k_mmo46, k_mmo47, k_mmo4]
mmo_creatures = mmolist[:] #Creates a seperate variable for use in the filter.
mmonumber = 0        


        #End of script


































         
