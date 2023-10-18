from odoo import models, fields, api
from datetime import timedelta

class ProductSalesAnalysis(models.TransientModel):
    _name = 'product.sales.analysis'

    start_date = fields.Date('Fecha de Inicio', required=True)
    end_date = fields.Date('Fecha de Fin', required=True)

    @api.multi
    def calculate_daily_sales(self):
        # Obtén todos los productos
        products = self.env['product.product'].search([])

        # Diccionario para almacenar la suma de las ventas diarias
        product_sales = {}

        for product in products:
            # Encuentra los movimientos de inventario de este producto en el rango de fechas
            stock_moves = self.env['stock.move'].search([
                ('product_id', '=', product.id),
                ('date', '>=', self.start_date),
                ('date', '<=', self.end_date),
                ('state', '=', 'done')
            ])

            # Filtra los movimientos de inventario que tuvieron stock
            stock_moves_with_stock = [move for move in stock_moves if move.product_qty > 0]

            # Calcula la suma de las ventas diarias para este producto
            total_sales = sum([move.product_qty for move in stock_moves_with_stock])

            # Calcula el número de días con stock
            days_with_stock = len(stock_moves_with_stock)

            # Calcula la media diaria de ventas
            if days_with_stock >= 60:
                daily_sales = total_sales / 60
            else:
                daily_sales = total_sales / days_with_stock

            product_sales[product.name] = daily_sales

        # Ahora tienes un diccionario con la media diaria de ventas para cada producto
        # Puedes almacenar estos resultados en un nuevo objeto o en cualquier otra forma que desees

        return True
