#eating cookies
    #if you don't account for negative values, if it bypasses zero, it will continue forever, hitting maximum recursion depth

    #runtime for eating_cookies is O(3^n)
        #at every point we are making 3 decisions
        #raising 3 to the power of number of inputs




#does cache exist and is the thing greater than zero (since we initialized everything to be zero we want to check if it's changed)
elif cache and cache[n] > 0:
    return cache[n]
else:
    if not cache:
        #must do n+1 to include n in our cache, otherwise not inclusive
        cache = [0 for _ in range(n+1)]
        cache = {i:0 for _ in range(n+1)}
    cache[n] = e_c(n-1, cache) + e_c(n-2, cache) + e_c(n-3, cache)
return cache[n]

#could also use an empty dictionary but you need to change the elif to test if cache[n] exists not if it's greater than 0

#runtime for e_c with cache is O(n). Space complexity does increase because we are adding a cache to keep track of.

#single number
    #if you delete anything that we already have in there then it might save us looping at the end. Would work for this problem as long as there are only pairs and one single