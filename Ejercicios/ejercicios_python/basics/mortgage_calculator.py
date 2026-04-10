# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
#%%
class Mortgage:
    def __init__(self, principal, annual_interest_rate, monthly_payment, loan_term_years, adelanta=0, adelanta_start_month=0, adelanta_end_month=0):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.monthly_payment = monthly_payment
        self.loan_term_years = loan_term_years
        self.adelanta = adelanta
        self.adelanta_start_month = adelanta_start_month
        self.adelanta_end_month = adelanta_end_month
        self.total_paid = 0.0
        self.current_month = 0

    @classmethod
    def calculate_monthly_interest(cls, annual_interest_rate):
        return annual_interest_rate / 12

    def monthly_payments_generator(self):
        monthly_interest = Mortgage.calculate_monthly_interest(self.annual_interest_rate)
        for _ in range(self.loan_term_years * 12):
            self.current_month += 1

            if self.adelanta_start_month < self.current_month <= self.adelanta_end_month:
                yield (self.monthly_payment + self.adelanta)
            else:
                yield self.monthly_payment

    def calculate_total_paid(self):
        payments = self.monthly_payments_generator()
        for payment in payments:
            self.principal = self.principal * (1 + self.calculate_monthly_interest(self.annual_interest_rate)) - payment
            self.total_paid += payment

    def display_result(self):
        print(f'Total paid: {round(self.total_paid, 2)}')


# Ejemplo de uso
mortgage = Mortgage(principal=500000.0, annual_interest_rate=0.05, monthly_payment=2684.11, loan_term_years=30, adelanta=1000, adelanta_start_month=6, adelanta_end_month=17)

mortgage.calculate_total_paid()
mortgage.display_result()

 
 #   """"David solicitó un crédito a 30 años para comprar una vivienda, 
 #   con una tasa fija nominal anual del 5%.
 #  Pidió $500000 al banco y acordó un pago mensual fijo de $2684"""
# Example of using the Mortgage class
davids_mortgage = Mortgage(principal=500000.0,
                            annual_interest_rate=0.05,
                             monthly_payment=2684.11,
                              loan_term_years=30,
                               adelanta=0,
                                adelanta_start_month=0,
                                adelanta_end_month=0)
davids_mortgage.calculate_total_paid()
davids_mortgage.display_result()

"""Ejercicio 1.8: Adelantos
        Supongamos que David adelanta pagos extra de $1000/mes,
        durante los primeros 12 meses de la hipoteca.
    """
# Example of using the Mortgage class
davids_mortgage = Mortgage(principal=500000.0,  
                             annual_interest_rate=0.05,
                             monthly_payment=2684.11,
                             loan_term_years=30 ,
                             adelanta=1000,
                             adelanta_start_month=12,
                             adelanta_end_month=0)
davids_mortgage.calculate_total_paid()
davids_mortgage.display_result()

        # """¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, 
        #   comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?"""
        # """Ejercicio 1.11: Bonus"""
# Example of using the Mortgage class
davids_mortgage = Mortgage(
    principal=500000.0,
    annual_interest_rate=0.05,
    monthly_payment=2684.11,
    loan_term_years=30,
    adelanta=1000,
    adelanta_start_month=60,
    adelanta_end_month=108
)

davids_mortgage.calculate_total_paid()
davids_mortgage.display_result()

# %%
