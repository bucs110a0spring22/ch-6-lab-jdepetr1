import turtle

def graph(upper = 1):
  '''
    Graphs the seq3np1 function from 'upper'
    args: upper (int) highest y-value on the graph
    return: None
  '''
  grapher = turtle.Turtle()
  writer = turtle.Turtle()
  wn = turtle.Screen()
  wn.setworldcoordinates(0,0,10,10)
  grapher.up()
  grapher.goto(0,0)
  grapher.down()
  writer.up()

  
  
  if upper < 0: 
    return 0
  max_so_far = [0,0]
  for start in range(1, upper+1):
    iters = seq3np1(start)
    if iters > max_so_far[1]:
      max_so_far = [start,iters]
    wn.setworldcoordinates(0,0,upper+10,max_so_far[1]+10)
    grapher.goto(start, iters)
    writer.goto(0, max_so_far[1])
    string = "Max so Far: " + str(max_so_far[0]) + ", " + str(max_so_far[1])
    writer.clear()
    writer.write(string)
    print("Current Loop:", start, "\n", "Num Iterations:", iters, "\n")

  wn.exitonclick()

def seq3np1(n):
  """
    Print the 3n+1 sequence from n, terminating when it reaches 1.
    args: n (int) starting value for 3n+1 sequence
    return: None
  """
  count = 0
  while(n != 1):
    
    if(n % 2) == 0:        # n is even
        n = n // 2
    else:                 # n is odd
        n = n * 3 + 1
    count += 1

  return count

def main():
  num = int(input("Input a positive integer that wil act as the upper bound of our range: "))
  graph(num)

main()
