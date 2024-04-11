

Basic web app using Flask python framework, bit of js, css and html

Reflections from task:
https://docs.google.com/document/d/1prn4CjPvmODBagAM-ICJKXluAP4D57OvZ7zupptZTpo/edit?usp=sharing

lots of repetition in the css, will be able to pull some of shared/duplicated rules out of the media queries
should probably finished other media query before refactoring

.gallery {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      max-width: 100%;
      gap: 1rem;
      margin: 2rem;

      .card {
        background-color: rgba(163, 60, 194, 0.5);
        border-radius: 7px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        padding-top: 10%;
        height: 75%;
        .card-top {
          display: flex;
          flex-direction: column;
          align-items: center;
          height: 50%;
          width: 100%;
          img {
            width: 75%;
            border-radius: 7px;
            height: 70%;
            margin-bottom: 2rem;
          }
          h3 {
            margin: 0 1rem;
            text-align: center;
          }
        }
        .card-bottom {
          display: flex;
          flex-direction: column;
          align-items: center;
          margin: 0 1rem;
          text-align: center;
          .opinions {
            display: flex;
            padding-bottom: 1.5rem;
            width: 100%;
            height: 5rem;
            justify-content: space-between;
            align-content: baseline;

            label {
              font-size: 2rem;
            }

            input[type="radio"]:checked + .emoji-not,
            input[type="radio"]:checked + .emoji-hot {
              font-size: 4rem;
            }
          }
        }
      }
    }