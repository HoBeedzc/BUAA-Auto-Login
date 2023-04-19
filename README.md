# Buaa Auto Login

> 本项目基于 [buaa-auto-login](https://github.com/zzdyyy/buaa_gateway_login) 二次开发

本项目更加安全、易用，无需在源文件中明文存储密码，并可实现自动登录，断网重连。

## 使用方法

将项目 clone 到本地
```bash
git clone https://github.com/HoBeedzc/BUAA-Auto-Login.git
```
进入项目目录
```bash
cd BUAA-Auto-Login
```
安装依赖
```bash
pip install -r requirements.txt
```

### 配置用户名与密码
可以选择两种方式，通过`config.toml`文件配置，或从环境变量中获取。

方法一： 修改 `config.toml` 中的用户名和密码和编码方式 (注意：如果使用明文密码，需要将 `encrypt` 设置为 `false`，务必保证此配置文件的安全性)

```toml
# username and password
username = "username"
password = "password"
encrypt = "true"
```
方法二（推荐）：将用户名与密码放在环境变量中

```bash
echo "export BUAA_USERNAME=username" >> ~/.bashrc
echo "export BUAA_PASSWORD=password" >> ~/.bashrc
```

### 启用登陆

方法一：
```bash
python main.py --config config.toml
```

方法二：
```bash
python main.py --config osenv
```

## 断网监控/自动重连

参考原仓库的 [README.md](https://github.com/zzdyyy/buaa_gateway_login#readme)