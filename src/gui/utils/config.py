from pathlib import Path

class Config:
    # 基础路径配置
    BASE_DIR = Path(__file__).parent.parent.parent.parent
    ASSETS_DIR = BASE_DIR / "assets"
    
    # 机器人模型配置
    ROBOT_MODEL_PATH = ASSETS_DIR / "xml/franka_emika_panda/panda.xml"
    
    # GUI 配置
    WINDOW_TITLE = "Genesis GUI"
    WINDOW_SIZE = "800x600"
    
    # 编辑器配置
    EDITOR_FONT = ("Courier", 12)
    EDITOR_BG = "#282c34"
    EDITOR_FG = "#abb2bf" 

    # Configuration settings for the robot control system

    # Default connection settings
    DEFAULT_PORT = 8080
    DEFAULT_HOST = "localhost"

    # Robot parameters
    MAX_SPEED = 1000
    MIN_SPEED = 0

    # GUI settings
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # Color definitions
    COLORS = {
        "background": "#FFFFFF",
        "text": "#000000",
        "button": "#EEEEEE"
    }