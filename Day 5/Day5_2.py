def SeatToBin(seat):
    seat_1Fs = seat.replace("F", "0")
    seat_1Ls = seat_1Fs.replace("L", "0")
    seat_0Bs = seat_1Ls.replace("B", "1")
    seat_0Rs = seat_0Bs.replace("R", "1")
    return seat_0Rs

seatIds = []

inputFile = open("Day 5/input.txt", "r")
inputList = inputFile.read().splitlines()

#For each line, get the row number and seat number
for line in inputList:
    id = (int(SeatToBin(line[0:7]), 2)*8) + int(SeatToBin(line[7:10]),2)
    seatIds.append(id)

seatIds.sort()
for i in range(1, len(seatIds)):
    seatDiff = seatIds[i] - seatIds[i-1]
    if seatDiff != 1:
        #We found out seat as al seats should have a difference of 1 unless it was ours
        #(because it wasn't included in the input)
        print (seatIds[i-1] + 1)