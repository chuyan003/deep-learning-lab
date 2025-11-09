'''
lesson6_app/
│
├─ app.py             # 主入口
├─ pages/
│   ├─ 1_home.py
│   ├─ 2_analysis.py
│   └─ 3_ai_tools.py
└─ config.yaml
Streamlit AI 平台框架
登录认证+多页导航
'''
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import Hasher

# ========== 加载配置文件 ==========
CONFIG_PATH = "lesson6_app/config.yaml"

with open(CONFIG_PATH, encoding="utf-8") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# ========== 登录界面 ==========
st.title("多页应用 + 用户登录系统")

authenticator.login(location="main")

if st.session_state["authentication_status"]:
    authenticator.logout("退出登录", "sidebar")
    st.sidebar.success(f"欢迎你，{st.session_state['name']}！")

    st.write("这是登录后的主界面。")

# ========== 注册新用户 ==========
with st.expander("注册新用户"):
    with st.form("register_form"):
        new_username = st.text_input("用户名")
        new_name = st.text_input("姓名")
        new_email = st.text_input("邮箱")
        new_password = st.text_input("密码", type="password")
        submitted = st.form_submit_button("注册")

    if submitted:
        if new_username in config['credentials']['usernames']:
            st.warning("用户名已存在，请选择其他用户名。")
        else:
            # 生成密码哈希
            hashed_pw = Hasher.hash(new_password)


            # 添加到配置
            config['credentials']['usernames'][new_username] = {
                "email": new_email,
                "name": new_name,
                "password": hashed_pw
            }

            # 保存到 config.yaml
            with open(CONFIG_PATH, "w", encoding="utf-8") as file:
                yaml.dump(config, file, default_flow_style=False)

            st.success(f"用户 {new_username} 注册成功，请返回登录界面。")

    elif st.session_state["authentication_status"] is False:
            st.error("用户名或密码错误")
    elif st.session_state["authentication_status"] is None:
            st.warning("请输入用户名和密码登录。")
