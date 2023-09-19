from playwright.sync_api import sync_playwright
from pages.mercado_libre import MercadoLibrePage

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        ml_page = MercadoLibrePage(page)
        ml_page.search("camisetas")

        results = []

        for _ in range(3):  # First 3 pages
            products = ml_page.get_products_from_current_page()
            for product in products:
                name, price, link = ml_page.extract_product_data(product)
                results.append((name, price, link))
            
            # Click to go to the next page
            page.click("a[title='Siguiente']")

        browser.close()

        # Save results to a file
        with open("results.txt", "w") as f:
            for name, price, link in results:
                f.write(f"{name}\n{price}\n{link}\n\n")

if __name__ == "__main__":
    main()
