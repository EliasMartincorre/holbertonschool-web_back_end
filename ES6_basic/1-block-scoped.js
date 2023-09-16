/* Given what you’ve read
 about var and hoisting, modify the variables
inside the function taskBlock so that the
variables aren’t overwritten inside the
conditional block */

export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  
  if (trueOrFalse) {
    // eslint-disable-next-line no-unused-vars
    const task = true;
    // eslint-disable-next-line no-unused-vars
    const task2 = false;
  }

  return [task, task2];
}
