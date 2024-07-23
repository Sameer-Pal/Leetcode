
class Solution:
  def countGoodNumbers(self, n: int) -> int:
    MOD = 10**9 + 7
    num_even = (n + 1) // 2
    num_odd = n // 2
    def mod_exp(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result
    result = (mod_exp(5, num_even, MOD) * mod_exp(4, num_odd, MOD)) % MOD
    return result