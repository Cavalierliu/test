## Docker容器的导入导出操作整理

### 方法1：容器的导入与导出(export和import)

#### 1、查看需要导出的容器

```
docker ps -a 
```

#### 2、导出export

导出后的tar文件传输至待导入机器上

```
docker export 容器名或者容器ID > 导出的路径以及tar包的名字  docker export centos> centos.tar 
```

#### 3、import导入

docker import tar包路径 自定义镜像名称 ：TAG (默认是latest)

```
docker import centos.tar test/centos 
```

到此新的机器上已经有一个新的镜像，可以用这个镜像直接生成容器了。



* 查看本机已有镜像：

  docker images

  

* 查看当前运行的所有容器
  docker ps -a

* .删除镜像（images），通过镜像（images）的id来指定删除谁
  docker rmi <image id>

docker build -t  ebox:v2 .





## 开启docker的容器

* 导入容器

  docker import veracruz_tz_root.tar veracruz

* 修改docker的tag

  sudo docker tag 86b60171f980 veracruz_image_tz:root

* 在docker目录下执行

  make tz-run

* 执行 sudo dokcer  ps 查看正在运行的docker

* 根据docker名字进入容器

  sudo docker exec -u root -it 'veracruz_tz_root' bash

* 配置环境

  export CARGO_HOME=/usr/local/cargo

  cd /work/rust-optee-trustzone-sdk/
  source environment
  source $CARGO_HOME/env

* 执行编译make trustzone



8. which sccache 查看目录

9. vim esc 按键U回退

10. ```
    [build]
    rustc-wrapper = "/usr/local/cargo/bin/sccache"
    ```

11. ```
    export RUSTC_WRAPPER=/usr/local/cargo/bin/sccache
    ```

11. 安装apq

12. 在/var/ww/html文件夹下面 创建软链接

13. sudo service apache2 restart

14. export 加环境变量

    例子：export  CARGO_NET_OFFLINE=true

    通过env 查看设置的环境变量是否成功

15. ssh -i C:\Users\MI\veracruzaws.pem ubuntu@18.183.246.182

16. TIBOE

18. export CARGO_HOME=/usr/local/cargo

19. ```
    source environment
    source $CARGO_HOME/env
    ```



pub trait xxx Send



tail -f /tmp/screenlog 