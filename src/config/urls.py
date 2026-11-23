"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# デフォルト設定を無効化
# from django.contrib import admin
# from django.urls import path

# 正規表現を使うルーティング関数
from django.urls import re_path

# Viewファイル（ハンドラー）をインポート
from presentation.http.supporting.hello.hello_view import HelloView

urlpatterns = [
    # デフォルト設定を無効化
    # path('admin/', admin.site.urls),
    # ルーティング追加
    re_path(r"^api/v1/hello/?$", HelloView.as_view()),
]
