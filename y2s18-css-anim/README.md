# CSS Animations Lab

# 0. Fork and Clone Repository

## 0.0 Fork the repository
As always, click on the "Fork" button in the top right of the page to fork the repo.

## 0.1 Go to your copy
Make sure your username comes before '/y2s18-css-anim' in the top left and/or the URL

## 0.2 Clone the repository
Using the terminal, go to your Desktop and clone the repo.

```
cd ~/Desktop
git clone <YOUR_REPO_URL>
cd y2s18-css-anim
```

# 1. Your First Animation

## 1.1 Make some `@keyframes`
- In `bounce_styles.css`, make a `@keyframes` component called `bounce`, with 2 frames, at 0% and 100%.

- Make it so the element has 0 opacity in the first frame and is scaled down to 1/10th of its usual size (using the `transform: scale()`) property

- Make the element be full-size and have opacity 1 in the final frame (the one labelled 100%)

## 1.2 Animate the circle
- In the CSS selector for the `svg` tag, add in the `animation` property

- Make the ball bounce for 2 seconds
  - If you need a hint, look at the lecture slides [here](http://go.meet.sh/anim-lec) and the reference website [here](https://robots.thoughtbot.com/css-animation-for-beginners)

## 1.3 Make it bounce infinitely
- Use `animation-iteration-count` property, or use the shorthand
  - If using the shorthand, remember to put values for the properties you aren't setting
  - Again, for hints, look at the [reference website](https://robots.thoughtbot.com/css-animation-for-beginners)