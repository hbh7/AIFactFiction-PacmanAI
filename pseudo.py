model = torch.nn.Sequential(
    ## Add initialization values for initial parameters
    ## Input Layer (Flattened (l x w) pixel input) (+ pacman direction?)
    ## Convolutions
    ## Output (n move from N moveset)
)

reward (**args):
    # Sum of points or points per move?
    reward = openAIGym output + custom rule input

# Ideal training
while True:
    # Play game using model
    while in Game:
        move = model(pixel input)
        train_model: # Train every move? How?
            predicted_reward = model_prediction 
            actual_reward = openAIGym output + custom rule input
            do_learning()

    # When Game is over
    reset Game
    iteration_counter++;

save_model():
    #do saving
