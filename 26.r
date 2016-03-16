recur.length <- function (n) {
  x = 1                             # Starting with the numerator 1
  remainders = c(x)
  
  repeat {
    x = (x*10) %% n                   # Find the remainder
    if (x == 0) { return (0) }        # Fraction terminates, so cycle length is 0.
    if ((x %in% remainders)) {break}  # Repeating remainder is found. Break from loop.
    remainders <- c(remainders, x)
    #print(remainders) # Else add remainder to list.
  }
  return (length(remainders) - which(remainders == x) + 1)  # Exclude non-repeating part of the decimal
}

k = c()
for (d in 1:999) {
  k = c(k,recur.length(d))
}

max(k)
which(k %in% max(k))
