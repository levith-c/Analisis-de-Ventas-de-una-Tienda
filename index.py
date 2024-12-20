import pandas as pd
import matplotlib.pyplot as plt

# Función para obtener los productos más vendidos
def productos_mas_vendidos(df):
    # Agrupar por producto y sumar las cantidades
    productos = df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False)
    return productos

# Función para generar un gráfico de barras de los productos más vendidos
def graficar_productos_mas_vendidos(productos_mas_vendidos):
    productos_mas_vendidos.head(10).plot(kind='bar', color='skyblue')
    plt.title("Top 10 Productos Más Vendidos")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad Vendida")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para calcular las ventas por vendedor
def ventas_por_vendedor(df):
    ventas = df.groupby('Vendedor')['Total'].sum().sort_values(ascending=False)
    return ventas

# Función para generar un gráfico de ventas por vendedor
def graficar_ventas_por_vendedor(ventas_por_vendedor):
    ventas_por_vendedor.plot(kind='bar', color='salmon')
    plt.title("Ventas Totales por Vendedor")
    plt.xlabel("Vendedor")
    plt.ylabel("Total de Ventas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para generar estadísticas generales
def resumen_estadisticas(df):
    total_ventas = df['Total'].sum()
    ventas_promedio = df['Total'].mean()
    productos_unicos = df['Producto'].nunique()
    return total_ventas, ventas_promedio, productos_unicos

# Función para generar un gráfico de torta para la distribución de ventas por producto
def graficar_distribucion_por_producto(df):
    ventas_por_producto = df.groupby('Producto')['Total'].sum()
    plt.figure(figsize=(8, 8))
    ventas_por_producto.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set3')
    plt.title("Distribución de Ventas por Producto")
    plt.ylabel('')  # Eliminar etiqueta del eje y
    plt.tight_layout()
    plt.show()

# Función principal para leer el archivo y realizar los análisis
def main():
    # Cargar los datos desde el archivo Excel
    df = pd.read_excel('C:\prueba\BD_VENTA.xlsx')

    # 1. Obtener los productos más vendidos
    productos_mas_vendidos_resultado = productos_mas_vendidos(df)
    print("Productos más vendidos:")
    print(productos_mas_vendidos_resultado)

    # 2. Graficar los productos más vendidos
    graficar_productos_mas_vendidos(productos_mas_vendidos_resultado)

    # 3. Calcular y mostrar ventas por vendedor
    ventas_por_vendedor_resultado = ventas_por_vendedor(df)
    print("\nVentas por Vendedor:")
    print(ventas_por_vendedor_resultado)

    # 4. Graficar ventas por vendedor
    graficar_ventas_por_vendedor(ventas_por_vendedor_resultado)

    # 5. Resumen de estadísticas generales
    total_ventas, ventas_promedio, productos_unicos = resumen_estadisticas(df)
    print(f"\nResumen Estadístico:")
    print(f"Total de ventas: ${total_ventas:.2f}")
    print(f"Ventas promedio por transacción: ${ventas_promedio:.2f}")
    print(f"Cantidad de productos únicos: {productos_unicos}")

    # 6. Graficar distribución de ventas por producto (Gráfico de torta)
    graficar_distribucion_por_producto(df)

# Llamada a la función principal
main()
