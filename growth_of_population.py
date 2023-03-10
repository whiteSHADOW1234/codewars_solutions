def nb_year(p0, percent, aug, p):
    percent = percent/100
    years = 0
    population = p0
    
    while(population < p):
        population = int(population + population * percent + aug)
        years += 1
        
    return years


# Alternative Solution
# def nb_year(p0, percent, aug, p):
#     years = 0
#     population = p0
    
#     while population < p:
#         population += int(population * percent / 100) + aug
#         years += 1
        
#     return years


def main():
    test_cases = [(1500, 5, 100, 5000), (1500000, 2.5, 10000, 2000000), (1500000, 0.25, 1000, 2000000)]
    for test_case in test_cases:
        result = nb_year(test_case[0], test_case[1], test_case[2], test_case[3])
        print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()
