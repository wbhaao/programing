def calculate_sechan_land_size(N, sizes):
    sizes.sort(reverse=True)
    sechan_land_size = 0

    while sizes:
        # Sechan's turn
        sechan_land_size += sizes.pop(0)

        if sizes:
            # Seungmo's turn
            sizes.pop(0)  # Remove the first land
            sechan_land_size *= 2

    return sechan_land_size

# Read the input
N = int(input())
sizes = [int(input()) for _ in range(N)]

# Calculate Sechan's land size
sechan_land_size = calculate_sechan_land_size(N, sizes)

# Print the result
print(sechan_land_size)
