import flet as ft
import json
import os
import datetime
from typing import Dict, Any

# --- CONFIG ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = SCRIPT_DIR
PORTFOLIO_FILE = os.path.join(BASE_DIR, "02_DATA", "portfolio_snapshot.json")
BANKING_FILE = os.path.join(BASE_DIR, "02_DATA", "banking_snapshot.json")

# --- THEME ---
BG = "#1e1e1e"
SURFACE = "#2d2d2d" 
ACCENT = "#3a7bd5"
TEXT = "#ffffff"
SUB = "#a0a0a0"
GREEN = "#00e676"
RED = "#ff5252"

def load_json(path: str) -> Dict[str, Any]:
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f: return json.load(f)
        except: return {}
    return {}

def main(page: ft.Page):
    page.title = "Finance One"
    page.bgcolor = BG
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 420
    page.window.height = 850
    page.padding = 0

    # Data
    p_data = load_json(PORTFOLIO_FILE)
    b_data = load_json(BANKING_FILE)

    t212 = p_data.get("cash", {}).get("total", 0.0)
    invested = p_data.get("cash", {}).get("invested", 0.0)
    bank = b_data.get("sparkasse_balance", 0.0) + b_data.get("revolut_balance", 0.0)
    net_worth = t212 + bank
    history = b_data.get("net_worth_history", [])

    # --- COMPONENTS ---
    def header(title: str):
        return ft.Container(
            content=ft.Text(title, size=28, weight=ft.FontWeight.BOLD),
            padding=ft.Padding(20, 40, 20, 10)
        )

    def card(title: str, val: float, sub: str, icon: ft.Icons):
        return ft.Container(
            content=ft.Column([
                ft.Row([ft.Icon(icon, color=ACCENT, size=20), ft.Text(title, color=SUB, size=14)]),
                ft.Text(f"{val:,.2f} €", size=22, weight=ft.FontWeight.BOLD),
                ft.Text(sub, size=12, color=SUB)
            ], spacing=5),
            bgcolor=SURFACE, border_radius=20, padding=20, width=260, height=130
        )

    def stock_row(pos: Dict):
        t = pos.get("ticker", "???")
        meta = p_data.get("metadata", {}).get(t, {})
        val = pos.get("quantity", 0) * pos.get("currentPrice", 0)
        ppl = pos.get("ppl", 0)
        col = GREEN if ppl >= 0 else RED
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Text(t[:2], weight="bold"), 
                    bgcolor=SURFACE, width=45, height=45, border_radius=12, 
                    alignment=ft.Alignment(0, 0)
                ),
                ft.Column([
                    ft.Text(meta.get("name", t), size=15, weight="bold", width=150, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text(f"{pos.get('quantity',0):.2f} • {meta.get('sector','ETF')}", size=12, color=SUB)
                ], expand=True),
                ft.Column([
                    ft.Text(f"{val:,.0f} €", weight="bold"), 
                    ft.Text(f"{ppl:+,.2f} €", color=col, size=12)
                ], alignment=ft.MainAxisAlignment.END)
            ]), 
            padding=ft.Padding(20, 10, 20, 10)
        )

    # --- VIEWS ---
    dashboard = ft.Column([
        header("Übersicht"),
        ft.Row([
            card("Net Worth", net_worth, "Gesamt", ft.Icons.ACCOUNT_BALANCE_WALLET),
            card("Depot", t212, f"Invest: {invested:,.0f} €", ft.Icons.SHOW_CHART),
            card("Bank", bank, "Liquidität", ft.Icons.SAVINGS),
        ], scroll=ft.ScrollMode.HIDDEN, spacing=15),
        ft.Container(ft.Text("Verlauf", size=20, weight="bold"), padding=ft.Padding(20, 20, 20, 10)),
        # Chart
        ft.Container(
            height=180, padding=ft.Padding(20, 0, 20, 0),
            content=ft.LineChart(
                data_series=[ft.LineChartData(
                    data_points=[ft.LineChartDataPoint(i, x["Total_Net_Worth"]) for i, x in enumerate(history[-15:])],
                    color=ACCENT, stroke_width=3, curved=True, below_line_bgcolor=ft.colors.with_opacity(0.1, ACCENT)
                )] if history else [],
                border=ft.border.all(0, ft.colors.TRANSPARENT),
                left_axis=ft.ChartAxis(labels_size=0), bottom_axis=ft.ChartAxis(labels_size=0),
                expand=True
            )
        )
    ], scroll=ft.ScrollMode.AUTO, expand=True)

    pos_sorted = sorted(p_data.get("positions", []), key=lambda x: x.get("quantity",0)*x.get("currentPrice",0), reverse=True)
    portfolio = ft.ListView([header("Portfolio")] + [stock_row(p) for p in pos_sorted], expand=True)

    div_controls = [header("Dividenden")]
    for d in sorted(p_data.get("future_divs", []), key=lambda x: x.get("pay_date") or "9999"):
        amt = d.get("amount", 0) * d.get("qty", 0)
        if amt < 0.01: continue
        name = p_data.get("metadata", {}).get(d["ticker"], {}).get("name", d["ticker"])
        div_controls.append(ft.Container(ft.Row([
            ft.Text(d["pay_date"][5:10], color=SUB, width=50),
            ft.Text(name, weight="bold", expand=True, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
            ft.Text(f"+{amt:.2f} €", color=GREEN, weight="bold")
        ]), padding=ft.Padding(20, 15, 20, 15)))
    dividends = ft.ListView(div_controls, expand=True)

    def on_nav(e):
        page.controls.clear()
        if e.control.selected_index == 0: page.add(dashboard)
        elif e.control.selected_index == 1: page.add(portfolio)
        elif e.control.selected_index == 2: page.add(dividends)
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.Icons.PIE_CHART_OUTLINE, selected_icon=ft.Icons.PIE_CHART, label="Portfolio"),
            ft.NavigationDestination(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, selected_icon=ft.Icons.CALENDAR_MONTH, label="Divs"),
        ],
        bgcolor=SURFACE, indicator_color=ACCENT, on_change=on_nav
    )

    page.add(dashboard)

if __name__ == "__main__":
    ft.app(main)