"""UI 自动化测试 demo: 打开页面、校验内容、模拟交互."""

from pathlib import Path

from playwright.sync_api import expect

# 本地测试页面（file:// 方式加载，无需联网，结果稳定）
DEMO_PAGE = (Path(__file__).parent / "demo.html").resolve().as_uri()


def test_open_local_page(page):
    """打开本地页面并校验标题与正文."""
    page.goto(DEMO_PAGE)
    page.wait_for_load_state("networkidle")

    # 断言标题
    expect(page).to_have_title("UI 自动化测试 Demo")

    # 断言 h1 内容
    expect(page.locator("h1")).to_have_text("Hello Playwright")

    # 断言正文可见
    expect(page.get_by_text("本地测试页面")).to_be_visible()

    print(f"\nPage title: {page.title()}")


def test_click_button(page):
    """模拟点击按钮并校验交互结果."""
    page.goto(DEMO_PAGE)
    page.wait_for_load_state("networkidle")

    # 点击按钮
    page.locator("#click-me").click()

    # 断言点击后出现的文本
    expect(page.locator("#result")).to_have_text("按钮已被点击")
