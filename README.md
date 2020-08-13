# AIFactFiction-PacmanAI

### To-Do

- [ ] Write Model
  - Based on / assisted by Microsoft analysis  
  - v0.1 by EOD 14/06/2020
  - Ivan?
  
- [ ] Write Reward Function
  - Points from game ( given by OpenAIGym ) + game rule edits
  - Will?
  
- [ ] Write Training Function
 - Rewrite Lab04 code ( reward / accuracy difference? )
 - Pytorch documentation reading
  
- [ ] Write Game Integration Function
  - Use model to play game ( run model on input and use chosen ouptut move as PacMan move )
  - Loop: Run model on frame -> use model's output move as input -> next frame
  - Hunter?
  
- [ ] Write Train->Play->Train->Play->... Loop
  - Simple loop of Training Function and Game Integration Function
  - As model improves more games, more data, longer training runs (reinforcement learning)
  
- [ ] Write save-load protocol
  - Mostly documentation reading, simple implementation
