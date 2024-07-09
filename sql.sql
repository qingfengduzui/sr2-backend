-- auto-generated definition
create table account
(
    id             int auto_increment
        primary key,
    studentID      varchar(8)               not null,
    name           varchar(5)               not null,
    phone          varchar(11) default '-1' not null,
    password       varchar(200)             not null,
    nickName       varchar(15)              not null,
    province       varchar(10)              not null,
    city           varchar(10)              not null,
    gender         varchar(3)               not null,
    political      varchar(8)               not null,
    education      varchar(36)              not null,
    dormitory      varchar(10)              not null,
    interests      varchar(10)              not null,
    fileData       varchar(100)             not null,
    favor          int                      null,
    qqsign         varchar(255)             null,
    email          varchar(255)             null,
    background     varchar(255)             null,
    jingxuanpic    varchar(255)             null,
    academy        varchar(50)              null,
    registerStatus int         default 1    null,
    constraint 学号
        unique (studentID)
);



-- auto-generated definition
create table announcement
(
    id          int auto_increment
        primary key,
    notice      varchar(255)                        not null,
    currentTime timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    status      int       default 1                 null,
    expire_time timestamp                           null
)
    comment '通告';



-- auto-generated definition
create table askforleave
(
    studentid   varchar(8)                          not null comment '学号',
    name        varchar(5)                          not null comment '姓名',
    currentTime timestamp default CURRENT_TIMESTAMP null comment '当前时间',
    days        int                                 not null comment '天数',
    major       varchar(50)                         not null comment '主修专业',
    reason      varchar(255)                        not null comment '请假原因',
    status      varchar(36)                         null,
    primary key (studentid, name, days)
)
    comment '请假表';



-- auto-generated definition
create table chatotm
(
    uid          int auto_increment
        primary key,
    id           varchar(36)                            null,
    message      varchar(200) default '-1'              not null,
    favor        int          default 0                 not null,
    createTime   datetime     default CURRENT_TIMESTAMP not null,
    nickName     varchar(15)  default '-1'              not null,
    fileData     varchar(100) default '-1'              not null,
    countcomment int          default 0                 not null
);




-- auto-generated definition
create table comments
(
    uid        int                                    not null comment '帖子编码',
    cid        int          default 1                 not null comment '回复id',
    comment    varchar(60)  default '-1'              not null,
    favor      int          default 0                 not null,
    rid        int          default 0                 not null comment '回复人id',
    createTime datetime     default CURRENT_TIMESTAMP not null,
    rcid       int          default -1                not null comment '引用的评论id',
    nickName   varchar(15)  default '-1'              not null,
    fileData   varchar(100) default '-1'              not null,
    primary key (cid, uid)
);




-- auto-generated definition
create table emotionalscore
(
    id        int auto_increment
        primary key,
    studentID varchar(8)    not null,
    name      varchar(5)    not null,
    email     varchar(255)  null,
    academy   varchar(50)   null,
    score     double        null,
    evaluate  int default 0 null
);




-- auto-generated definition
create table exchangedormitory
(
    studentid    varchar(8)                          not null comment '学号',
    name         varchar(5)                          not null comment '姓名',
    olddormitory varchar(10)                         not null comment '旧宿舍号',
    newdormitory varchar(10)                         not null comment '新宿舍号',
    currentTime  timestamp default CURRENT_TIMESTAMP null,
    major        varchar(50)                         not null comment '学院',
    reason       varchar(255)                        not null comment '申请理由',
    status       varchar(36)                         null,
    primary key (studentid, name, olddormitory, newdormitory)
)
    comment '更换宿舍申请表';




-- auto-generated definition
create table favor
(
    id  int not null,
    uid int not null,
    primary key (id, uid)
);




-- auto-generated definition
create table favorcomment
(
    id  int not null,
    uid int not null,
    cid int not null,
    primary key (id, uid, cid)
);




-- auto-generated definition
create table vehicle
(
    studentid   varchar(8)                          not null comment '学号',
    name        varchar(5)                          not null comment '姓名',
    major       varchar(36)                         not null comment '学院',
    currentTime timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '当前时间',
    time        date                                not null comment '申请时间',
    reason      varchar(255)                        not null comment '原因',
    status      varchar(36)                         null,
    license     varchar(36)                         null,
    id          int auto_increment
        primary key
)
    comment '车辆进入预约';




-- auto-generated definition
create table webiogin
(
    manager  varchar(50) not null,
    major    varchar(20) not null comment '专业',
    password varchar(36) not null comment '密码',
    primary key (manager, major)
)
    comment '网页登录管理';




-- auto-generated definition
create table webqa
(
    id        int auto_increment
        primary key,
    question  varchar(255) default '1' not null,
    answer    varchar(255) default '1' not null,
    studentid varchar(36)              null,
    status    varchar(36)              null
)
    comment 'webQS';

