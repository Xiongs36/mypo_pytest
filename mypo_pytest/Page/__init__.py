#搜索按钮
from selenium.webdriver.common.by import By

loc_set=By.ID,'com.android.settings:id/search'
#输入搜索内容
loc1_input=By.ID,'android:id/search_src_text'
loc_return=By.CLASS_NAME,'android.widget.ImageButton'