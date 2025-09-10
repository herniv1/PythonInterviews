from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# -----------------------------
# Configuración de Selenium
# -----------------------------
driver = webdriver.Chrome()

def extraer_tabla_por_titulo(nombre_tab, archivo_csv):
    """
    Busca un <h3 class="hiddenHeader"> con el texto nombre_tab
    y extrae la tabla que aparece después.
    """
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Buscar el header
    header = soup.find("h3", class_="hiddenHeader", string=nombre_tab)
    if not header:
        print(f"⚠️ No se encontró el encabezado {nombre_tab}")
        return

    # Buscar la primera tabla después del header
    tabla = header.find_next("table")
    if not tabla:
        print(f"⚠️ No se encontró la tabla de {nombre_tab}")
        return

    # Extraer filas
    filas = tabla.find_all("tr")
    encabezados = [th.get_text(strip=True) for th in filas[0].find_all("th")]
    registros = []

    for fila in filas[1:]:  # saltar encabezado
        celdas = [c.get_text(strip=True) for c in fila.find_all("td")]
        if celdas:
            registros.append(celdas)

    # Guardar en CSV
    with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(encabezados)
        writer.writerows(registros)

    print(f"✅ Datos de {nombre_tab} guardados en {archivo_csv}")


try:
    driver.get("https://lmb.com.mx/estadisticas")
    time.sleep(5)  # esperar que cargue scripts iniciales

    # -----------------------------
    # Manejar popup de cookies
    # -----------------------------
    try:
        aceptar_cookies = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'aceptar')]"))
        )
        aceptar_cookies.click()
        print("✔ Popup de cookies cerrado")
        time.sleep(1)  # esperar que desaparezca
    except:
        print("No se encontró popup de cookies")

    # -----------------------------
    # Extraer Bateo y Pitcheo
    # -----------------------------
    extraer_tabla_por_titulo("Bateo", "bateo.csv")
    extraer_tabla_por_titulo("Pitcheo", "pitcheo.csv")

finally:
    driver.quit()