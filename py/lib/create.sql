# -*- coding: utf-8 -*-  

/*
序号    int
日期    char 16
编号    char 32
其他    char 64
*/


/* 序号表
*/
CREATE TABLE  qx_sequence (
  s_name CHAR(32), 
  s_value int, 
  s_comment CHAR(128),
  PRIMARY KEY(s_name ASC)
);


/* 数据导入临时表
*/
CREATE TABLE  temp_data (
  data_no char(32) not null,
  data_type char(32) not null,
  use_flag char(32 not null,
  c1 CHAR(128), 
  c2 CHAR(128), 
  c3 CHAR(128), 
  c4 CHAR(128), 
  c5 CHAR(128), 
  c6 CHAR(128), 
  c7 CHAR(128), 
  c8 CHAR(128), 
  c9 CHAR(128), 
  c10 CHAR(128), 
  c11 CHAR(128), 
  c12 CHAR(128), 
  c13 CHAR(128), 
  c14 CHAR(128), 
  c15 CHAR(128), 
  c16 CHAR(128), 
  c17 CHAR(128), 
  c18 CHAR(128), 
  c19 CHAR(128), 
  c20 CHAR(128) 
);

/* 机型代码表
*/
CREATE TABLE phone_info (
  phone_name CHAR(64) NOT NULL, 
  phone_no   CHAR(64) NOT NULL,
  PRIMARY KEY(phone_name ASC)
);


/* 发料单
fld_no, 客户名称，客户地址，联系电话，所属地市，需求单号，流水号
，制单日期，出库日期，发料仓库，金额大写，金额合计
*/
CREATE TABLE fld (
  fld_no CHAR(32) NOT NULL, 
  khmc CHAR(64), 
  khdz CHAR(128), 
  lxdh CHAR(64), 
  ssds CHAR(64), 
  xqdh CHAR(64), 
  lsh  CHAR(64),
  zdrq CHAR(16), 
  ckrq CHAR(16), 
  flck CHAR(64),
  jedx CHAR(64),
  jehj CHAR(64),
  PRIMARY KEY(fld_no ASC)
);

/*
fld_no, 编号，名称及规格，计量单位，应发数量，实发数量，备注
*/
CREATE TABLE fld_list (
  fld_no CHAR(32) NOT NULL, 
  bh INT NOT NULL, 
  mcjgg CHAR(64), 
  jxdm CHAR(32), 
  jldw CHAR(16), 
  yfsl CHAR(16), 
  sfsl CHAR(16), 
  bz CHAR(64)
);

/*
insert into fld(fld_no, xmh, xm, mc, ssds, dz, flbh, zdrq, ckrq, flck ) 
       values ('1111','001','促销项目','华为','渭南','渭南东大街','陕006','2012-05-12','2012-05-12','东仓库');
insert into fld_list(fld_no, wzbh, mcjgg, jldw, fcsl, jxbm, dj, kh, dh ) values ('1111','1','华为909','台','100','hw909','300','渭南分公司','13991300000');
*/


/*  收料单
syd_no, 合同号，供料单位，收料依据
，项目号，收料编号，发票号
，制单日期，收料日期，收料仓库
*/
CREATE TABLE sld (
  sld_no CHAR(32) NOT NULL, 
  hth CHAR(32), 
  gldw CHAR(64), 
  slgj CHAR(64), 
  xmh CHAR(32), 
  slbh CHAR(32), 
  fph CHAR(32), 
  zdrq CHAR(16), 
  slrq CHAR(16), 
  slck CHAR(64), 
  PRIMARY KEY(sld_no ASC)
);

/*
sld_no, 物资编号，名称及规格，计量单位
，交货数量，实收数量，盈，亏，新旧程度
，购入单价，购入金额，备注
*/
CREATE TABLE sld_list (
  sld_no CHAR(32) NOT NULL, 
  wzbh INT NOT NULL, 
  mcjgg CHAR(64), 
  jldw CHAR(16), 
  jhsl INT, 
  sssl INT, 
  ying CHAR(16), 
  kui CHAR(16), 
  xjcd CHAR(16), 
  grdj INTEGER, 
  grje INTEGER, 
  bz CHAR(64)
);

/*  缴料单
jld_no, 缴料依据，收料根据
，缴料编号，收料仓库
，缴料日期，收料日期
*/
CREATE TABLE jld (
  jld_no CHAR(32) NOT NULL, 
  jlyj CHAR(64), 
  slgj CHAR(64), 
  jlbh CHAR(32), 
  slck CHAR(64), 
  jlrq CHAR(16), 
  slrq CHAR(16), 
  bz CHAR(64), 
  PRIMARY KEY(jld_no ASC)
);

/*
jld_no, 编号，名称及规格，计量单位
，缴料，实收，新旧程度，件数
*/
CREATE TABLE jld_list (
  jld_no CHAR(32) NOT NULL, 
  bh INT NOT NULL, 
  mcjgg CHAR(64), 
  jldw CHAR(16), 
  jl INT, 
  ss INT, 
  xjcd CHAR(16), 
  js INTEGER
);

/*  领用单
lyd_no, 领料单位，领料类别，
领用单编号，领料仓库，领料日期
*/
CREATE TABLE lyd (
  lyd_no CHAR(32) NOT NULL, 
  llbh CHAR(64), 
  lllb CHAR(64), 
  lydbh CHAR(32), 
  llck CHAR(64), 
  llrq CHAR(16), 
  PRIMARY KEY(lyd_no ASC)
);

/*
lyd_no, 编号，名称及规格，计量单位
应发数量，实发数量，新旧程度，用途
*/
CREATE TABLE lyd_list (
  lyd_no CHAR(32) NOT NULL, 
  bh INT NOT NULL, 
  mcjgg CHAR(64), 
  jldw CHAR(16), 
  yfsl INT, 
  sfsl INT, 
  xjcd CHAR(16), 
  yt CHAR(64)
);



/* 内部调拨单
nbdbd_no, 单据号，填制日期，拨出库房，拨入仓库，收货联系人
，联系人电话，收货地址，收货日期
*/
CREATE TABLE nbdbd (
  nbdbd_no CHAR(32) NOT NULL, 
  djbh CHAR(64), 
  tzrq CHAR(16), 
  bckf CHAR(64), 
  brck CHAR(64), 
  shlxr CHAR(32), 
  lxrdh CHAR(32), 
  shdz CHAR(128), 
  shrq CHAR(16), 
  PRIMARY KEY(nbdbd_no ASC)
);

/*
nbdbd_no, 序号，名称及规格，颜色，拨出数量，
拨入数量，调拨依据，备注
*/
CREATE TABLE nbdbd_list (
  nbdbd_no CHAR(32) NOT NULL, 
  xh INT NOT NULL, 
  mcjgg CHAR(64), 
  ys CHAR(16), 
  bcsl INT, 
  brsl INT, 
  dbyj CHAR(64), 
  bz CHAR(64)
);

/*  入库单
rkd_no, 合同号，供货单位
，入库单号，收料仓库
，收料日期
*/
CREATE TABLE rkd (
  rkd_no CHAR(32) NOT NULL, 
  hth CHAR(32), 
  ghdw CHAR(64), 
  rkdh CHAR(32), 
  slck CHAR(64), 
  slrq CHAR(16), 
  PRIMARY KEY(rkd_no ASC)
);

/*
rkd_no, 编号，名称及规格型号，计量单位
应收数量，实收数量，新旧程度，件数，备注
*/
CREATE TABLE rkd_list (
  rkd_no CHAR(32) NOT NULL, 
  bh INT NOT NULL, 
  mcjgg CHAR(64), 
  jldw CHAR(16), 
  yssl INT, 
  sssl INT, 
  xjcd CHAR(16), 
  js INT, 
  bz CHAR(64)
);



insert into rkd(rkd_no, hth, ghdw, rkdh, slck, slrq ) values ('1','001','华为','rq002','东仓库','2012-05-12');


insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','1','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','2','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','3','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','4','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','5','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','6','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','7','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','8','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','9','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','10','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','11','华为909','台','100','90','新','1','备注 2012-05-12');
insert into rkd_list(rkd_no, bh, mcjgg, jldw, yssl, sssl, xjcd, js, bz ) values ('1','12','华为909','台','100','90','新','1','备注 2012-05-12');


