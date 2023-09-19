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
        name_element = product.query_selector("h2.ui-search-item__title")
        name = name_element.text_content() if name_element else None
    
        price_element = product.query_selector("span.price-tag-amount")
        price = price_element.text_content() if price_element else None
    
        link_element = product.query_selector("a.ui-search-item__group__element.ui-search-link")
        link = link_element.get_attribute("href") if link_element else None
    
        return name, price, link
