# Kris-Tof Dice Toss

there are two labs in here, one for Java and one for Python.

pick your poison. do one or the other.

- [Java](./java)
- [Python](./python)

## Development Strategy: Building Incrementally

When tackling this dice simulation project, resist the urge to implement everything at once. Instead, follow a methodical approach that breaks the problem into manageable pieces:

### Start Small, Build Outward

Begin with the core simulation loop - the heart of your program. Get a simple version working that can:
1. Create a basic dice object
2. Roll it once
3. Display the result

Don't worry about bins, statistics, or complex features yet. Focus on getting this minimal loop functional first. Once you can reliably roll a die and see output, you've established your foundation.

### Add Functionality Step by Step

After your basic loop works, expand incrementally:

1. **Add multiple dice**: Modify your loop to handle rolling multiple dice per iteration
2. **Introduce bins**: Create a simple bin structure to collect results
3. **Implement counting**: Track how many times each sum appears
4. **Add statistics**: Calculate and display percentages or probabilities
5. **Enhance output**: Improve formatting and add visual elements like histograms

Each step should be fully functional before moving to the next. This approach lets you catch issues early and ensures you always have a working version.

### Test-Driven Development

Unit testing is crucial for this project. Write tests for your core classes before or alongside implementation:

**For Dice class:**
- Test that dice roll within expected ranges (1-6 for standard dice)
- Verify that multiple rolls produce different results over time
- Test edge cases like invalid die sizes

**For Bins class:**
- Test that bins correctly increment counts
- Verify that retrieving counts returns accurate values
- Test boundary conditions (minimum/maximum possible sums)

Example test structure:
```
testDiceRollRange() - ensure all rolls are 1-6
testDiceRandomness() - verify distribution over many rolls
testBinIncrement() - check that bins count correctly
testBinRetrieval() - verify getting counts works
```

### Benefits of This Approach

This incremental strategy offers several advantages:
- **Easier debugging**: Problems are isolated to small, recent changes
- **Confidence building**: Regular success maintains momentum
- **Better design**: Each iteration reveals what the next step truly needs
- **Flexibility**: Easy to pivot or add features without rewriting everything

### Common Pitfalls to Avoid

- Don't build the entire class hierarchy upfront - start simple
- Avoid perfectionism - get something working, then improve it
- Don't skip testing - bugs compound as complexity grows
- Resist feature creep - implement core functionality first

Remember: a simple, working simulation is infinitely more valuable than a complex, broken one. Start small, test often, and build incrementally toward your final solution.


