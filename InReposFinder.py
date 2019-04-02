import json
import requests

request = input("Please enter request: ")
print("searching...")
# https://github.blog/2013-05-16-personal-api-tokens/
token = "enter_your_token"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
headersAuth = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Authorization': 'token ' + token
}

loadPage = lambda url, header: requests.get(url, headers=header).text

loadPage("https://api.github.com", headersAuth)

# for 1.13
l = map(lambda i: i.replace('https://github.com/', ''),
        ['https://github.com/mezz/JustEnoughItems', 'https://github.com/progwml6/ironchest',
         'https://github.com/TehNut/HWYLA', 'https://github.com/Funwayguy/OreExcavation',
         'https://github.com/squeek502/AppleSkin', 'https://github.com/jaredlll08/Controlling',
         'https://gitlab.com/DragonForge/HammerCore', 'https://github.com/way2muchnoise/BetterAdvancements',
         'https://github.com/mezz/ModNameTooltip', 'https://github.com/VsnGamer/ElevatorMod',
         'https://github.com/TehNut/Harvest', 'https://github.com/lumien231/QuickLeafDecay',
         'https://gitlab.com/Zeitheron/SolarFluxReborn', 'https://github.com/Tschipp/CarryOn',
         'https://github.com/M4thG33k/TombManyGraves2', 'https://github.com/zlainsama/CosmeticArmorReworked',
         'https://github.com/SilentChaos512/SilentLib', 'https://github.com/MC-U-Team/Useful-Backpacks',
         'https://github.com/MC-U-Team/U-Team-Core', 'https://github.com/AtomicStryker/atomicstrykers-minecraft-mods',
         'https://github.com/sokratis12GR/TheDragonLib', 'https://gitlab.com/CDAGaming/CraftPresence',
         'https://github.com/AtomicStryker/atomicstrykers-minecraft-mods',
         'https://github.com/SilentChaos512/ScalingHealth', 'https://github.com/SilentChaos512/SilentGems',
         'https://github.com/Darkhax-Minecraft/Enchantment-Descriptions', 'https://github.com/SquidDev-CC/CC-Tweaked',
         'https://github.com/shedaniel/RoughlyEnoughItems', 'https://github.com/sci4me/Torcherino',
         'https://github.com/BuiltBrokenModding/SBM-woodenShears',
         'https://github.com/portablejim/Additional-Resources', 'https://github.com/blay09/PrettyBeaches',
         'https://github.com/portablejim/Audio-Death', 'https://github.com/Drullkus/Shield-Parry',
         'https://github.com/Darkhax-Minecraft/AdditionalBanners', 'https://github.com/kjmaster1/InventoryGenerators',
         'https://gitlab.com/DragonForge/ImprovableSkills', 'https://github.com/ate47/XrayRift',
         'https://github.com/JackyyTV/SimpleSponge', 'https://github.com/maruohon/itemscroller',
         'https://github.com/blay09/ForgivingVoid', 'https://github.com/davidmaamoaix/TinyMobFarm',
         'https://github.com/Lemonszz/SimpleTeleporters', 'https://github.com/gbl/DurabilityViewer',
         'https://github.com/Tfarcenim/OverloadedArmorBar', 'https://github.com/dmillerw/MineMenu',
         'https://github.com/Clownvin/Just-A-Few-More-Ores', 'https://github.com/gigaherz/ToolBelt',
         'https://github.com/gigaherz/PackingTape', 'https://github.com/lumien231/Chunk-Animator',
         'https://github.com/JanneSoon/EnhancedArmaments', 'https://gitlab.com/DragonForge/SimpleQuarry',
         'https://github.com/chylex/Better-Sprinting', 'https://github.com/maruohon/malilib',
         'https://github.com/Clownvin/Living-Enchantment', 'https://github.com/TheRandomLabs/VanillaDeathChest',
         'https://github.com/maruohon/litematica', 'https://github.com/Laton95/Pyramid-Plunder',
         'https://github.com/GirafiStudios/BetterTitleScreen', 'https://github.com/Gaz492/Player-Plates',
         'https://github.com/Insane-96/VulcaniteMod', 'https://github.com/Tamaized/AoV',
         'https://github.com/SilentChaos512/Equipment-Tooltips', 'https://github.com/Lemonszz/trap-expansion',
         'https://github.com/dmillerw/Ping', 'https://github.com/SilentChaos512/FunOres',
         'https://github.com/VladoCC/get_back_home', 'https://github.com/Insane-96/Carbonado',
         'https://github.com/PanSzelescik/moreplates', 'https://github.com/bl4ckscor3/Sit',
         'https://github.com/PanSzelescik/morelibs', 'https://github.com/MrMarnic/AnimalNet',
         'https://github.com/Rumaruka/SimpleGrinder', 'https://gitlab.com/sargunv-mc-mods/level-up-hp',
         'https://github.com/shedaniel/Rift-ModList', 'https://github.com/Cadiboo/NoCubes',
         'https://bitbucket.org/hrznstudio/albedo', 'https://github.com/zlainsama/CleanView',
         'https://github.com/LCoreModders/Regeneration', 'https://github.com/SuperheroesX-Dev/SuperheroesX',
         'https://github.com/gbl/EasierVillagerTrading', 'https://github.com/zlainsama/OfflineSkins',
         'https://github.com/BatHeart/batty-ui-forge', 'https://github.com/ichttt/FirstAid',
         'https://github.com/ThexXTURBOXx/Rift-WorldInfo', 'https://github.com/gigaherz/InventorySpam',
         'https://github.com/Cadiboo/RenderChunk-rebuildChunk-Hooks', 'https://github.com/Dalarion/Croparia2.0',
         'https://github.com/Lemonszz/LemonLib', 'https://github.com/MJRLegends/Space-Astronomy-Tweaks',
         'https://github.com/Lemonszz/BetterCompass', 'https://github.com/ate47/cursormod',
         'https://github.com/stfwi/engineers-decor', 'https://github.com/bl4ckscor3/GlobalXP',
         'https://github.com/SilentChaos512/Silent-Gear', 'https://github.com/Shadows-of-Fire/AttainedDrops2',
         'https://github.com/pentantan/JapariCraftMod', 'https://github.com/xfl03/MCCustomSkinLoader',
         'https://github.com/irtimaled/BoundingBoxOutlineReloaded', 'https://github.com/Parker8283/BowInfinityFix',
         'https://github.com/MasterGeneral156/CTD-Core', 'https://github.com/Tfarcenim/Toughness-Bar',
         'https://github.com/ichttt/McPaint', 'https://github.com/alcatrazEscapee/ore-veins',
         'https://github.com/Mickeyxiami/NonUpdate', 'https://github.com/Iunius118/ToLaserBlade',
         'https://github.com/Shadows-of-Fire/EnderBags', 'https://github.com/Corail31/recycler',
         'https://github.com/MoreThanHidden/RestrictedPortals', 'https://github.com/gbl/EasierCrafting',
         'https://github.com/Da-Technomancer/Essentials', 'https://github.com/Selim042/SM-Selim-Enchants',
         'https://github.com/maruohon/minihud', 'https://github.com/ArnoSaxena/buildhelper',
         'https://github.com/mrburger/Beta-Plus', 'https://github.com/AtomicStryker/atomicstrykers-minecraft-mods',
         'https://github.com/MasterGeneral156/MoGlowstone-Mod', 'https://github.com/BuiltBrokenModding/SBM-boneTorch',
         'https://github.com/joshiejack/CopyPaste', 'https://github.com/maruohon/tweakeroo',
         'https://github.com/TheRandomLabs/RandomConfigs', 'https://github.com/zlainsama/PeacefulSurface',
         'https://github.com/jmilthedude/FreeLook', 'https://github.com/BuiltBrokenModding/SBM-Merpig',
         'https://github.com/TheIllusiveC4/CakeChomps', 'https://github.com/gbl/EasierChests',
         'https://github.com/stal111/Compressed-Items', 'https://github.com/dmillerw/PassthroughSigns',
         'https://github.com/CammiePone/ArtemisLib', 'https://github.com/The-Fireplace-Minecraft-Mods/Mob-Rebirth',
         'https://github.com/redBullSlurpie/SlurpiesDongles', 'https://github.com/arthurbambou/Painting-Mod',
         'https://github.com/Andromander/Nifty', 'https://github.com/SilentChaos512/TorchBandolier',
         'https://github.com/trikzon/Snow-Variants', 'https://github.com/JackyyTV/NoAutoJump',
         'https://github.com/Pyre540/following-villagers', 'https://github.com/gbl/Grid',
         'https://github.com/Hugman76/Mubble', 'https://github.com/Clownvin/Everyone-Poops',
         'https://github.com/bl4ckscor3/Scarecrows', 'https://github.com/shedaniel/CustomSelectionBox-New',
         'https://github.com/Crimix/ServerTabInfo', 'https://github.com/Krevik/ExpOreMod',
         'https://github.com/bl4ckscor3/BiomeInfo', 'https://github.com/HenryLoenwind/middletorch',
         'https://github.com/rdvdev2/TimeTravelMod', 'https://github.com/bl4ckscor3/ChanceGlobe',
         'https://github.com/blay09/Fertilization', 'https://github.com/BuiltBrokenModding/SBM-LizardDogo',
         'https://github.com/Tfarcenim/AerialAffinity', 'https://github.com/bl4ckscor3/The-Plopper',
         'https://github.com/ErdbeerbaerLP/Creative-Fireworks', 'https://github.com/bl4ckscor3/Snowmancy',
         'https://gitlab.com/sargunv-mc-mods/always-drop-loot', 'https://github.com/gbl/FlightHelper',
         'https://github.com/BuiltBrokenModding/SBM-Punt-Animal', 'https://github.com/ErdbeerbaerLP/1.13-gamemode1-Mod',
         'https://github.com/TheIllusiveC4/Curios', 'https://github.com/bl4ckscor3/LenientCreepers',
         'https://github.com/DoubleDoorDevelopment/GlobalSettings',
         'https://github.com/BuiltBrokenModding/SBM-Growmeal',
         'https://github.com/The-Fireplace-Minecraft-Mods/Grand-Economy', 'https://github.com/autaut03/kottle',
         'https://github.com/TheIllusiveC4/CustomFoV', 'https://github.com/gigaherz/signbutton',
         'https://github.com/m4rcmonde/Simple-Macros', 'https://github.com/marcus8448/GamemodeOverhaul',
         'https://github.com/TheIllusiveC4/CuriousShulkerBoxes', 'https://github.com/BuiltBrokenModding/SBM-SnowPower',
         'https://github.com/The-Fireplace-Minecraft-Mods/Block-Replacer', 'https://github.com/LotuxPunk/OpenBackup',
         'https://github.com/bl4ckscor3/WoolPlates', 'https://github.com/secretdataz/ThaiFixes-Fabric',
         'https://github.com/Qelifern/IronFurnaces', 'https://github.com/Selim042/Bob-Ross-Mod',
         'https://github.com/JayJay1989/GameSenseSDK',
         'https://github.com/The-Fireplace-Minecraft-Mods/Turtle-Shell-Drop',
         'https://github.com/The-Fireplace-Minecraft-Mods/Clans', 'https://github.com/Hialus/NotEnoughKeys',
         'https://github.com/TheIllusiveC4/CurioOfUndying', 'https://github.com/TheIllusiveC4/CustomNausea',
         'https://github.com/The-Fireplace-Minecraft-Mods/Grand-Exchange',
         'https://github.com/TheIllusiveC4/CuriousElytra', 'https://github.com/Axeryok/CocoaInput',
         'https://github.com/ochotonida/squash', 'https://github.com/funniray/Mixer',
         'https://github.com/LotuxPunk/AutoAfkKicker', 'https://github.com/TheIllusiveC4/Caelus',
         'https://github.com/blutmondgilde/BlutmondRPG', 'https://github.com/DarkRoleplay/DRP---Global-Data-Pack',
         'https://github.com/TyrellPlayz/Big-Industries', 'https://github.com/BuiltBrokenModding/SBM-DualWither',
         'https://github.com/TheFloydman/LinkingBooks', 'https://github.com/LotuxPunk/AutoMessageDisplayerForge',
         'https://github.com/handicraftsman/almondcraft', 'https://github.com/Cypher121/Kettle',
         'https://github.com/TheSledgeHammer/GroovyForge', 'https://github.com/rdvdev2/TensorFlowAddon',
         'https://github.com/KillerMapper/EmbellishCraft', 'https://github.com/SilentChaos512/Treasure-Bags'])

flatten = lambda l: [item for sublist in l for item in sublist]


def getLinkToFile(url):
    answer = loadPage(url, headers)
    j = json.loads(answer)
    return j.get("html_url")


def find(repo):
    answer = loadPage("https://api.github.com/search/code?q=" + request + "+repo:" + repo, headers)
    j = json.loads(answer)
    items = j.get("items")
    if items != None:
        return list(map(lambda i: getLinkToFile(i.get("url")), items))
    else:
        return []


res = flatten([find(repo) for repo in l])
for i in res:
    print(i)
