# 简介

这是一个战舰世界的 **神乐Mea** 语音MOD
暂时缺失：CV语音、快捷指令、消耗品语音


# 如何使用

- 将banks置入res_mods/0.9.x.x/
- 启动游戏

# 修改MOD
只需要将相应的音频文件（统一增益为0dB，如有特殊情况需要继续增大）转换为wem格式，并且按以下目录结构放置，使用工具生成xml文件即可。
```
└─Voice
    ├─Autopilot
    │  ├─Autopilot__Checkpoint
    │  ├─Autopilot__End
    │  ├─Autopilot__Off
    │  └─Autopilot__On
    ├─Avatar_Damage
    │  └─Debuff__CriticalFlooding
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
    │  └─HelpType__Engine
    ├─Last_Hope
    ├─LetsBatlle
    ├─quick_commands
    │  └─quick_commands__CMD_QUICK_NO_WAY
    ├─Result
    │  └─Result__Lose
    ├─Teamkill_punishment
    ├─Timer5
    └─Torpedo_Danger
        ├─Torpedo_Location__Torpedo_Ahead
        ├─Torpedo_Location__Torpedo_Back
        ├─Torpedo_Location__Torpedo_Left
        └─Torpedo_Location__Torpedo_Right
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
Project - Project Settings - Source Settings
Default Conversion Settings: Verbis Quality High
![更改格式.gif](https://i.loli.net/2020/03/23/tJqfQWIjPRD8XNb.gif)
- 转换文件
Project - Convert All Audio Files
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
