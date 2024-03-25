![image](https://github.com/MananChandna/Command-line-tool/assets/139998502/9bede363-353f-44da-9140-579f53609b25)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Command-Line Tool: Stack Overflow Scraper</h1>
    <p>This command-line tool allows you to scrape Stack Overflow questions based on specific tags and filters.</p>
    
  <h2>Usage</h2>
    <p>To use the tool, you need to have Python installed on your system. Follow these steps:</p>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/MananChandna/Command-line-tool</code></pre>
        <li>Navigate to the project directory:</li>
        <pre><code>cd your-repo</code></pre>
        <li>Install the required dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Run the command-line tool:</li>
        <pre><code>python script.py --tag TAG --query_filter FILTER --num_pages NUM_PAGES --output_file OUTPUT_FILE</code></pre>
    </ol>

  <h2>Arguments</h2>
    <ul>
        <li><code>--tag TAG</code>: Specify the tag for Stack Overflow questions (default: python)</li>
        <li><code>--query_filter FILTER</code>: Specify the query filter for sorting questions (default: Votes)</li>
        <li><code>--num_pages NUM_PAGES</code>: Specify the number of pages to scrape (default: 1)</li>
        <li><code>--output_file OUTPUT_FILE</code>: Specify the output file name (default: output.csv)</li>
    </ul>

  <h2>Example</h2>
    <p>Scrape top Python questions sorted by votes for 5 pages and save the results to python_questions.csv:</p>
    <pre><code>python script.py --tag python --query_filter Votes --num_pages 5 --output_file python_questions.csv</code></pre>

  <h2>Author</h2>
    <p>Created by Manan Chandna. Find me on Linkedin: <a href="https://www.linkedin.com/in/manan-chandna-697588257/">Manan</a></p>
</body>
</html>
