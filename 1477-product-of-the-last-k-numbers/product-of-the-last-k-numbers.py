class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]  # To handle product queries conveniently
        self.reset_needed = False  # To track if we've encountered a zero

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]  # Reset because the product of anything with 0 is 0
        else:
            # Multiply the last product with the new number
            self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k: int) -> int:
        # We just need to divide the last product by the one before the k numbers
        if k >= len(self.prefix_product):
            return 0  # This should not happen based on problem constraints
        return self.prefix_product[-1] // self.prefix_product[-1 - k]
