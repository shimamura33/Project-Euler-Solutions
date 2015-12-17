# Brute force
# Takes at least 15 minutes to run this loop so should never attempt the brute force to get 
k=c()
for (i in 1:80000) {
  k=c(k,as.numeric(strsplit(as.character(i), "")[[1]]))
}

k[1]*k[10]*k[10^2]*k[10^3]*k[10^4]*k[10^5]*k[10^6]

