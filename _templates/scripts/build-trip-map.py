#!/usr/bin/env python3
"""build-trip-map.py — 通用 trip-map 页面生成器（地址链版）

Usage:
    python3 build-trip-map.py [--data DATA.json] [--out OUTPUT.html]

默认读 example-data.json（内蒙环线示例），输出到 ../../当前目录
"""
import argparse
import json
import urllib.parse
from pathlib import Path

GROUP_ORDER = [
    ("景点", "🏛", ["attract", "start", "end", "stop"]),
    ("餐厅", "🍜", ["food"]),
    ("酒店", "🏨", ["hotel"]),
    ("服务区 / 加油站", "⛽", ["service"]),
]
TAG_LABEL = {
    "attract": "景点",
    "hotel": "酒店",
    "food": "餐厅",
    "service": "服务区",
    "start": "起点",
    "end": "终点",
    "stop": "驿站",
}


def render_poi(item, default_city, src_tag):
    """福建模式（混合）：按 coords 字段切换按钮形态。

    - 有 coords（精确经纬度）：
      btn-nav = navigation?to=lng,lat,name → 🚗 导航
      btn-search = marker?markers=lng,lat,name → 📍 标记位置

    - 无 coords（仅地址名）：
      btn-nav = search?keyword=POI名&city=城市 → 🔍 搜索
      btn-search 留空（无坐标不能生成 marker）
    """
    name = item["name"]
    addr = item["addr"]
    tag = item["tag"]
    info = item.get("info", "")
    coords = item.get("coords")  # 可选 [lng, lat]
    encoded_name = urllib.parse.quote(name)

    has_coord = bool(coords and len(coords) == 2)

    if has_coord:
        lng, lat = coords[0], coords[1]
        nav_url = f'https://uri.amap.com/navigation?to={lng},{lat},{encoded_name}&mode=car&src={src_tag}'
        marker_url = f'https://uri.amap.com/marker?markers={lng},{lat},{encoded_name}&src={src_tag}'
        nav_label = '🚗 导航'
        actions_html = (
            f'<a class="btn-nav" target="_blank" href="{nav_url}">{nav_label}</a>'
            f'\n        <a class="btn-search" target="_blank" href="{marker_url}">📍 标记位置</a>'
        )
    else:
        nav_url = f'https://uri.amap.com/search?keyword={encoded_name}&city={default_city}&src={src_tag}'
        nav_label = '🔍 搜索'
        actions_html = (
            f'<a class="btn-nav" target="_blank" href="{nav_url}">{nav_label}</a>'
        )

    return f'''    <div class="poi">
      <div class="poi-name">{name}
        <span class="tag {tag}">{TAG_LABEL.get(tag, "POI")}</span>
      </div>
      <div class="poi-info">📍 {info}</div>
      <div class="poi-actions">
        {actions_html}
      </div>
    </div>'''


def render_day(day, default_city, src_tag):
    items = day["items"]
    groups = {}
    for grp_name, _, types in GROUP_ORDER:
        for it in items:
            if it["tag"] in types:
                groups.setdefault(grp_name, []).append(it)

    groups_html = []
    for grp_name, emoji, types in GROUP_ORDER:
        if grp_name not in groups:
            continue
        pois_html = "\n".join(render_poi(p, default_city, src_tag) for p in groups[grp_name])
        groups_html.append(f'''  <!-- {grp_name} -->
  <div class="group">
    <div class="group-title"><span class="emoji">{emoji}</span>{grp_name}</div>

{pois_html}
  </div>''')

    return f'''<section class="day" id="{day["id"]}">
  <div class="day-title">
    <span class="day-num">{day["date"]}</span>
    <div class="day-info">
      <h2>{day["title"]}</h2>
      <div class="meta">{day["meta"]}</div>
    </div>
    <span class="route-arrow">→</span>
  </div>

{chr(10).join(groups_html)}
</section>'''


def render_day_nav(days):
    items = []
    for d in days:
        short = d["date"] + " " + d["title"].split("→")[0].split(" ")[0].strip()
        items.append(f'  <a href="#{d["id"]}">{short}</a>')
    return "\n".join(items)


HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<title>🚗 {title}</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ -webkit-text-size-adjust: 100%; }}

body {{
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  font-size: 15px;
  line-height: 1.5;
  color: #1a1a1a;
  background: #f5f6f8;
  padding-bottom: 60px;
  -webkit-font-smoothing: antialiased;
}}
header {{
  background: linear-gradient(135deg, #FF6F00 0%, #FF8F00 100%);
  color: white; padding: 20px 18px 18px; position: sticky; top: 0; z-index: 100;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}}
header h1 {{ font-size: 18px; font-weight: 600; margin-bottom: 6px; }}
header p {{ font-size: 12px; opacity: 0.95; }}
header p .route {{ font-weight: 600; }}
.day-nav {{
  background: white; padding: 10px 12px; overflow-x: auto; white-space: nowrap;
  position: sticky; top: 76px; z-index: 99; border-bottom: 1px solid #e8eaec;
  -webkit-overflow-scrolling: touch;
}}
.day-nav::-webkit-scrollbar {{ display: none; }}
.day-nav a {{
  display: inline-block; padding: 6px 12px; margin-right: 6px;
  background: #f0f1f3; color: #555; border-radius: 14px;
  text-decoration: none; font-size: 12px; font-weight: 500;
}}
.day-nav a.active, .day-nav a:active {{ background: #FF6F00; color: white; }}
.day {{ padding: 16px 14px; }}
.day-title {{
  display: flex; align-items: center; margin-bottom: 14px; padding: 10px 14px;
  background: linear-gradient(to right, #fff5e6, white); border-left: 5px solid #FF6F00;
  border-radius: 4px;
}}
.day-title .day-num {{ font-size: 20px; font-weight: 700; color: #FF6F00; margin-right: 10px; }}
.day-title .day-info {{ flex: 1; }}
.day-title h2 {{ font-size: 15px; font-weight: 600; color: #1a1a1a; margin-bottom: 2px; }}
.day-title .meta {{ font-size: 11px; color: #888; }}
.day-title .route-arrow {{ font-size: 16px; color: #FF6F00; font-weight: 600; }}
.group {{ margin-bottom: 18px; }}
.group-title {{
  font-size: 13px; font-weight: 600; color: #555; margin-bottom: 8px; padding: 0 4px;
  display: flex; align-items: center;
}}
.group-title .emoji {{ margin-right: 6px; font-size: 15px; }}
.poi {{
  background: white; border-radius: 10px; padding: 12px 14px;
  margin-bottom: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); border: 1px solid #ecedef;
}}
.poi-name {{
  font-size: 15px; font-weight: 600; color: #1a1a1a; margin-bottom: 4px;
  display: flex; align-items: center; justify-content: space-between;
}}
.poi-name .tag {{
  font-size: 10px; font-weight: 500; padding: 2px 7px;
  border-radius: 10px; white-space: nowrap; margin-left: 8px;
}}
.tag.attract   {{ background: #fef0ef; color: #c7392b; }}
.tag.hotel     {{ background: #f0ecfa; color: #6b46c1; }}
.tag.food      {{ background: #fff5e8; color: #d97706; }}
.tag.service   {{ background: #e0f0fc; color: #2563eb; }}
.tag.start     {{ background: #e8f5e9; color: #2d7d46; }}
.tag.end       {{ background: #fce4ec; color: #c62828; }}
.tag.stop      {{ background: #e3f2fd; color: #1565c0; }}
.poi-info {{ font-size: 12px; color: #888; margin-bottom: 10px; line-height: 1.5; }}
.poi-actions {{ display: flex; gap: 8px; }}
.poi-actions a {{
  flex: 1; display: block; text-align: center;
  padding: 8px 6px; border-radius: 6px;
  text-decoration: none; font-size: 13px; font-weight: 500;
  -webkit-tap-highlight-color: transparent;
}}
.btn-nav {{ background: #FF6F00; color: white; }}
.btn-search {{ background: #f0f1f3; color: #555; }}
.usage {{
  background: white; padding: 16px; border-radius: 10px;
  margin: 16px 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}}
.usage h3 {{ font-size: 15px; font-weight: 600; margin-bottom: 8px; color: #FF6F00; }}
.usage ol {{ padding-left: 22px; font-size: 13px; color: #555; line-height: 1.7; }}
.usage .tip {{
  margin-top: 10px; font-size: 12px; color: #888;
  padding: 8px 10px; background: #fff8e1; border-radius: 6px;
}}
.to-top {{
  position: fixed; bottom: 20px; right: 20px;
  width: 44px; height: 44px; border-radius: 50%;
  background: #FF6F00; color: white; border: none;
  font-size: 18px; font-weight: 600;
  box-shadow: 0 3px 10px rgba(0,0,0,0.2); cursor: pointer; z-index: 50;
}}
</style>
</head>
<body>

<header>
  <h1>🚗 {title}</h1>
  <p><span class="route">{tagline}</span></p>
  <p style="margin-top:4px;">{subtitle}</p>
</header>

<nav class="day-nav" id="dayNav">
{day_nav}
</nav>

{days_html}

<section class="usage">
  <h3>📱 使用说明</h3>
  <ol>
    <li><b>点击任意点位的【🚗 导航】或【🔍 搜索】按钮</b></li>
    <li>手机会自动唤起高德地图 App</li>
    <li>确认起点（默认当前定位）+ 终点，开始导航</li>
    <li>在 App 里可切换驾车 / 步行 / 公交</li>
    <li>如未装高德 App，会自动跳转到网页版地图</li>
  </ol>
  <div class="tip">
    💡 小贴士：<br>
    • 提前下载高德地图 App，登录账号开启路径记录<br>
    • 离线地图下载：行程涉及省份（自驾无忧）<br>
    • 颜色编码：🔴 景点 · 🟣 酒店 · 🟠 餐厅 · 🔵 服务区
  </div>
</section>

<button class="to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>

<script>
const navLinks = document.querySelectorAll('.day-nav a');
const sections = document.querySelectorAll('.day');

navLinks.forEach(link => {{
  link.addEventListener('click', (e) => {{
    navLinks.forEach(l => l.classList.remove('active'));
    e.target.classList.add('active');
  }});
}});

const observer = new IntersectionObserver((entries) => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      const id = entry.target.id;
      navLinks.forEach(l => {{
        l.classList.toggle('active', l.getAttribute('href') === '#' + id);
      }});
    }}
  }});
}}, {{ rootMargin: '-30% 0px -50% 0px' }});

sections.forEach(s => observer.observe(s));
</script>

</body>
</html>
'''


def main():
    parser = argparse.ArgumentParser(description="trip-map 页面生成器")
    parser.add_argument("--data", default="example-data.json", help="数据 JSON 路径")
    parser.add_argument("--out", default=None, help="输出 HTML 路径（默认用 data.output 字段）")
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        # 尝试脚本同级目录
        script_dir = Path(__file__).parent
        alt = script_dir / args.data
        if alt.exists():
            data_path = alt
        else:
            print(f"❌ 找不到数据文件: {args.data}")
            return 1

    with open(data_path) as f:
        data = json.load(f)

    default_city = data.get("default_city", "")
    src_tag = data.get("src_tag", "momotrip")
    output = args.out or data.get("output")

    days_html = "\n\n".join(render_day(d, default_city, src_tag) for d in data["days"])
    day_nav = render_day_nav(data["days"])

    html = HTML_TEMPLATE.format(
        title=data["title"],
        tagline=data["tagline"],
        subtitle=data["subtitle"],
        day_nav=day_nav,
        days_html=days_html,
    )

    if output:
        out_path = Path(output)
        if not out_path.is_absolute():
            # 相对当前工作目录
            out_path = Path.cwd() / output
        with open(out_path, "w") as f:
            f.write(html)
        print(f"✅ 写入: {out_path}")

    poi_count = sum(len(d["items"]) for d in data["days"])
    print(f"📊 POI 总数: {poi_count}")
    for d in data["days"]:
        print(f"   {d['date']}: {len(d['items'])} 个 POI")
    return 0


if __name__ == "__main__":
    exit(main())
