import random

def spawn_enemies(coordinate_list):
  """Spawns enemies at random locations on the map, or near the character if they are close to an enemy spawn point.

  Args:
    coordinate_list: A list of coordinates where the character should be dropped off from the plane.

  Returns:
    A list of enemy spawn points.
  """

  enemy_spawn_points = []
  for coordinate in coordinate_list:
 
    for enemy_spawn_point in enemy_spawn_points:
      if distance(coordinate, enemy_spawn_point) < ENEMY_SPAWN_RADIUS:
        
        enemy_spawn_points.append(enemy_spawn_point)
        break

    
    if len(enemy_spawn_points) == 0:
      enemy_spawn_points.append(random.choice(MAP_COORDINATES))

  return enemy_spawn_points

def check_if_character_died(coordinate_list):
  """Checks if the character died after being dropped off from the plane.

  Args:
    coordinate_list: A list of coordinates where the character should be dropped off from the plane.

  Returns:
    True if the character died, False otherwise.
  """


  enemy_spawn_points = spawn_enemies(coordinate_list)


  for enemy_spawn_point in enemy_spawn_points:
    if distance(coordinate_list[-1], enemy_spawn_point) < ENEMY_SPAWN_RADIUS:
     
      return True

  
  return False


ENEMY_SPAWN_RADIUS = 100
MAP_COORDINATES = [(x, y) for x in range(1000) for y in range(1000)]


coordinate_list = []
while True:
  coordinate = input("Enter a coordinate: ")
  if coordinate == "exit":
    break
  coordinate_list.append(coordinate)


if check_if_character_died(coordinate_list):
  print("Character died.")
else:
  print("Character survived.")
