# 简介

这是一个战舰世界的 **神乐Mea** 语音MOD
<br>
暂时缺失：CV语音、快捷指令、消耗品语音


# 如何使用

- 将banks置入res_mods/0.9.x.x/
- 启动游戏

# 修改MOD
只需要将相应的音频文件（统一增益为0dB，如有特殊情况需要继续增大）转换为wem格式，并且按以下目录结构放置，使用工具生成xml文件即可<br>
具体文件用途可以[参考FBK语音包](https://forum.worldofwarships.asia/topic/38024-all-shirakami-fubuki-voice-mod-hololive-vtuber/)（才不是因为懒得写文档）
```
Voice
├─Autopilot
│  ├─Autopilot__Checkpoint
│  ├─Autopilot__End
│  ├─Autopilot__Off
│  └─Autopilot__On
├─Avatar_Damage
│  └─Debuff__CriticalFlooding
├─Blue_Stripe
├─Death
├─Detection_enemy
│  ├─DetectionEnemy__AirCarrier
│  ├─DetectionEnemy__Battleship
│  ├─DetectionEnemy__Cruiser
│  ├─DetectionEnemy__Destroyer
│  ├─DetectionEnemy__Multi
│  └─DetectionEnemy__Submarine
├─DominationStatus
│  ├─Domination__D_Ally
│  ├─Domination__D_Enemy
│  ├─Domination__W_Ally
│  └─Domination__W_Enemy
├─DoubleKill
├─Fire
│  └─isPlayer__True
├─FirstKill
├─Frags
│  ├─isPlayer__False
│  │  ├─Frag_Type__AirCarrier
│  │  ├─Frag_Type__Battleship
│  │  ├─Frag_Type__Cruiser
│  │  ├─Frag_Type__Destroyer
│  │  └─Frag_Type__Submarine
│  └─isPlayer__True
│      ├─Frag_Type__AirCarrier
│      ├─Frag_Type__Battleship
│      ├─Frag_Type__Cruiser
│      ├─Frag_Type__Destroyer
│      └─Frag_Type__Submarine
├─FriendlyHit
├─GoodHit
├─Help
│  ├─HelpType__AirDefenseDisp
│  ├─HelpType__CallFighters
│  ├─HelpType__Engine
│  ├─HelpType__Fighter
│  ├─HelpType__Hydroacoustic
│  ├─HelpType__Scout
│  └─HelpType__Smoke
├─Help_End
│  ├─HelpType__AirDefenseDisp
│  ├─HelpType__CrashCrew
│  ├─HelpType__Engine
│  ├─HelpType__Fighter
│  ├─HelpType__Scout
│  └─HelpType__Smoke
├─Help_Interrupted
│  ├─HelpType__Fighter
│  └─HelpType__Scout
├─Last_Hope
├─LetsBatlle
├─MGshot
├─Pilots_Status
│  ├─Plane_Type__Bomber
│  │  ├─PlaneStatus__ATTACK_STARTED
│  │  ├─PlaneStatus__LANDING_INITIATED
│  │  ├─PlaneStatus__TAKEOFF_ENDED
│  │  └─PlaneStatus__UNDER_ATTACK
│  ├─Plane_Type__Fighter
│  │  ├─PlaneStatus__ATTACK_STARTED
│  │  ├─PlaneStatus__LANDING_INITIATED
│  │  ├─PlaneStatus__TAKEOFF_ENDED
│  │  └─PlaneStatus__UNDER_ATTACK
│  └─Plane_Type__Torpedo
│      ├─PlaneStatus__ATTACK_STARTED
│      ├─PlaneStatus__LANDING_INITIATED
│      ├─PlaneStatus__TAKEOFF_ENDED
│      └─PlaneStatus__UNDER_ATTACK
├─quick_commands
│  ├─quick_commands__CMD_QUICK_AYE_AYE
│  ├─quick_commands__CMD_QUICK_BACK
│  ├─quick_commands__CMD_QUICK_BACK_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_CARAMBA
│  ├─quick_commands__CMD_QUICK_GOOD_GAME
│  ├─quick_commands__CMD_QUICK_GOOD_GAME_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_GOOD_LUCK
│  ├─quick_commands__CMD_QUICK_NEED_AIR_DEFENCE
│  ├─quick_commands__CMD_QUICK_NEED_SMOKE
│  ├─quick_commands__CMD_QUICK_NEED_SUPPORT
│  ├─quick_commands__CMD_QUICK_NEED_SUPPORT_ALLY_PLANE
│  ├─quick_commands__CMD_QUICK_NEED_SUPPORT_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_NEED_VISION
│  ├─quick_commands__CMD_QUICK_NO_WAY
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_BASE
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_BUILDING
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_PLANE
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_POINT
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_BASE
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_BUILDING
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_PLANE
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_POINT
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_SHIP
│  ├─quick_commands__CMD_QUICK_THANK_YOU
│  └─quick_commands__CMD_QUICK_THANK_YOU_ALLY_SHIP
├─quick_commands_receive
│  ├─quick_commands__CMD_QUICK_AYE_AYE
│  ├─quick_commands__CMD_QUICK_BACK
│  ├─quick_commands__CMD_QUICK_BACK_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_CARAMBA
│  ├─quick_commands__CMD_QUICK_GOOD_GAME
│  ├─quick_commands__CMD_QUICK_GOOD_GAME_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_GOOD_LUCK
│  ├─quick_commands__CMD_QUICK_NEED_AIR_DEFENCE
│  ├─quick_commands__CMD_QUICK_NEED_SMOKE
│  ├─quick_commands__CMD_QUICK_NEED_SUPPORT
│  ├─quick_commands__CMD_QUICK_NEED_VISION
│  ├─quick_commands__CMD_QUICK_NO_WAY
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_BASE
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_BUILDING
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_PLANE
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_POINT
│  ├─quick_commands__CMD_QUICK_TACTIC_ALLY_SHIP
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_BASE
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_BUILDING
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_PLANE
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_POINT
│  ├─quick_commands__CMD_QUICK_TACTIC_ENEMY_SHIP
│  ├─quick_commands__CMD_QUICK_THANK_YOU
│  └─quick_commands__CMD_QUICK_THANK_YOU_ALLY_SHIP
├─Result
│  ├─Result__Draw
│  ├─Result__Lose
│  └─Result__Win
├─TAshot
├─Teamkill_punishment
├─Timer5
├─TorpedoHit
├─Torpedo_Danger
│  ├─Torpedo_Location__Torpedo_Ahead
│  ├─Torpedo_Location__Torpedo_Back
│  ├─Torpedo_Location__Torpedo_Left
│  └─Torpedo_Location__Torpedo_Right
├─UI_Defective_Modules
│  ├─ModuleType__Engine
│  │  └─ModuleState__Crit
│  ├─ModuleType__MainGun
│  │  ├─ModuleState__Crit
│  │  └─ModuleState__Dead
│  ├─ModuleType__StreeringWheel
│  │  └─ModuleState__Crit
│  └─ModuleType__TorpedoGun
│      └─ModuleState__Dead
└─WOWS_Weather_ChangedFXSS
    ├─Weather__Snowstorm
    └─Weather__Storm
```
## 如何制作wem文件
- 下载并安装Wwise
- 将需要转换的音频统一音量，并且按照wav格式保存到相应的文件夹下
- 启动Wwise
![启动.gif](https://i.loli.net/2020/03/23/bjgcyizS74TEtUZ.gif)
- 新建项目
![新建.gif](https://i.loli.net/2020/03/23/fZrlnxj7NDO3CVU.gif)

- 保持目录结构导入wav文件
![导入.gif](https://i.loli.net/2020/03/23/Kf2UDEalnyVrIkJ.gif)

- 更改输出格式
Project - Project Settings - Source Settings<br>
Default Conversion Settings: Verbis Quality High
![更改格式.gif](https://i.loli.net/2020/03/23/tJqfQWIjPRD8XNb.gif)

- 转换文件
Project - Convert All Audio Files<br>
转换后的文件位于 Documents/WwiseProjects/**ProjectName**/.cache/Windows/SFX
![转换.gif](https://i.loli.net/2020/03/23/rwsDXzKcZM2yQfE.gif)

- 因为转换后的文件被添加了后缀，所以我们需要使用自动重命名软件删除掉后缀
![更名.gif](https://i.loli.net/2020/03/23/Rp4iKVWlmHevOna.gif)

## 生成XML文件
1. 打开modxmlgenerator-0.8.8文件夹
2. 运行modxmlgenerator.exe
3. 输入MOD文件夹所在路径
![批注 2020-03-23 141448.png](https://i.loli.net/2020/03/23/6xoC1O4l2SyspD9.png)

4. 运行后会自动生成mod.xml
5. 使用相同方法运行modxmlupdater.exe
6. 运行后会生成mod.xml与mod.xml.bak

# 许可
遵循GPLv3
