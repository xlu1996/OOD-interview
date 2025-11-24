from abc import ABC, abstractmethod

# 1. Define the Interface
class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass


# 2. Concrete Implementations
class StripePayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Stripe: ${amount}")
        # In real implementation: API calls to Stripe
        return {"status": "success", "provider": "Stripe"}


class RazorpayPayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Razorpay: ₹{amount}")
        # In real implementation: API calls to Razorpay
        return {"status": "success", "provider": "Razorpay"}


class PayPalPayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via PayPal: ${amount}")
        # In real implementation: API calls to PayPal
        return {"status": "success", "provider": "PayPal"}


# 3. Service that depends on the interface
class CheckoutService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def set_payment_gateway(self, payment_gateway):
        """Allows switching payment gateway at runtime"""
        self.payment_gateway = payment_gateway
    
    def checkout(self, amount):
        """Process checkout using the injected payment gateway"""
        print(f"\n--- Starting checkout for ${amount} ---")
        result = self.payment_gateway.initiate_payment(amount)
        print(f"Payment result: {result}")
        return result


# 4. Usage Example
if __name__ == "__main__":
    # Create payment gateway instances
    stripe_gateway = StripePayment()
    razorpay_gateway = RazorpayPayment()
    paypal_gateway = PayPalPayment()
    
    # Create checkout service with Stripe
    checkout_service = CheckoutService(stripe_gateway)
    checkout_service.checkout(120.50)
    
    # Switch to Razorpay at runtime
    checkout_service.set_payment_gateway(razorpay_gateway)
    checkout_service.checkout(150.50)
    
    # Switch to PayPal
    checkout_service.set_payment_gateway(paypal_gateway)
    checkout_service.checkout(200.00)