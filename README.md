# TurengScraper
TurengScraper is a tool to scrape the Turkish-English dictionary website, [tureng.com](https://tureng.com/).

<br/><br/>

## The story of the Scraper and the Quiz App
Back in 2017, when I was new to creating Android apps, a friend told me about Oxford's selected [3000 English words](https://www.oxfordlearnersdictionaries.com/about/oxford3000) for learners. I thought it would be a good idea to create a quiz app to help people learn these words. The Quiz app became my second attempt at building an application with my limited knowledge and experience, and I published it on the Google Play Store. The app was on the market for some time, but I eventually discontinued it due to the lack of attention it received.

After several years, I decided to revive the project and make it better this time. This was an opportunity for me to see how far I had come. The scraper is the first part of reviving the project, and why I needed it is pretty obvious if we take a look at the old database:

<p align="center">
  <img width="400.5" height="284.25 " src="https://user-images.githubusercontent.com/45321194/235388600-fb3c9e9c-bd9a-4583-97e0-f9f8651c1749.png">
</p>

Being inexperienced, the app that I built was insufficient in every way, especially when it came to the most important aspect: the database. Back then, I manually created a database containing more than 3800 English words, but the real problem was that some words had multiple meanings, and my database only contained one Turkish equivalent for each word. It was frustrating to create a database by hand, and I remember feeling suffocated even before finishing the first column of Turkish equivalent words. It was impossible for me to add more columns to the database table.

Now, I have decided that the first step of reviving the project is to enrich the database. The database must contain multiple meanings of a word, and putting this data together is easier than ever with the help of the old database table and the TurengScraper tool. The tool fetches a word from the old database table "WORDS," searches for the word on tureng.com, scrapes the first five meanings, and writes them to a new database table called "dictionary." The new database table looks like this:

<p align="center">
  <img width="849.75 " height="281.25 " src="https://user-images.githubusercontent.com/45321194/235388718-e56007da-1848-46de-b7f4-a4ba9ba23f25.png">
</p>

The tool also keeps the column "wrong_answers" on the new database table because I remember choosing words that were likely to confuse or trick people while answering the quiz. By the way, the old app contained only two options for each word - one wrong and one correct option - but I'm planning to change it so that the quiz will have more options depending on the difficulty level. Generating wrong options will be easier with the denser database table made possible by the scraper.

The next step is to refactor the Android app written in Java. I plan to share the source code on GitHub and publish the app on the Google Play Store. Stay tuned!
