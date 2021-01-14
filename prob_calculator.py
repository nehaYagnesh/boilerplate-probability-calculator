import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **hat):
        self.contents = list()
        for color,ball_count in hat.items():
            while ball_count != 0:
                self.contents.append(color)
                ball_count -= 1
        # print('Content_List', self.contents)

    def draw(self, num_balls_drawn):
        ball_drawn = list()
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:    
            while num_balls_drawn != 0:
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                ball_drawn.append(random_ball)
                num_balls_drawn -= 1
            # print('Ball drawn',ball_drawn)
            return ball_drawn
 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob_c = 0
    for exp in range(num_experiments):
        hat_ = copy.deepcopy(hat)
        ball_drawn_list = hat_.draw(num_balls_drawn)
        ball_drawn_dict = {color: ball_drawn_list.count(color) for color in set(ball_drawn_list)}
        
        match_found = True
        for color,value in expected_balls.items():
            if (color in ball_drawn_dict
                and expected_balls[color] <= ball_drawn_dict[color]):
                continue
            else:
                match_found = False    

        if match_found:
            prob_c += 1
    return prob_c/num_experiments
