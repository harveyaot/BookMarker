[User]
id               // 主键
email            // 注册邮箱
password         // 注册密码
username         // 用户昵称，@username可以唯一标识一个用户
avatarImage      // 用户头像
registerTime     // 注册时间
lastAccessTime   // 最后一次访问时间


[Tag]
id               // 主键
name             // tag名称


[Url]
id               // 主键
url              // 链接地址
title            // 网页标题
abstract         // 网页摘要

[UserUrl]
id               // 主键
user             // User表外键
url              // Url表外键
note             // 收藏时写的注释
time             // 收藏时间


[UserUrlTag]
id               // 主键
user             // User表外键
url              // Url表外键
tag              // Tag表外键
time             // 打tag时间

