   import os


   def apply_discount(amount, percent):
       # Эта строка специально сделана очень длинной, чтобы нарушить правило flake8 про 80 символов
       return amount - amount * percent / 100
