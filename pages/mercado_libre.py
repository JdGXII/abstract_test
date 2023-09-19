from playwright.sync_api import Page

class MercadoLibrePage:
    def __init__(self, page: Page):
        self.page = page
    
    def search(self, query: str):
        self.page.goto("https://www.mercadolibre.com.pe")
        self.page.fill("input[placeholder='Buscar productos, marcas y más…']", query)
        self.page.press("input[placeholder='Buscar productos, marcas y más…']", "Enter")

    def get_products_from_current_page(self):
        return self.page.query_selector_all("li.ui-search-layout__item")

    def extract_product_data(self, product):
        name = product.text_content("h2.ui-search-item__title")
        price = product.text_content("span.price-tag-amount")
        link = product.get_attribute("href", "a.ui-search-item__group__element.ui-search-link")
        return name, price, link
