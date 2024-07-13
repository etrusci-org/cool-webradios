<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cool Webradios</title>
    <style>
        /* VARS ------------------------------------------------ */
        :root {
            --font-family: Georgia, 'Times New Roman', serif;
            --text-color: hsl(0, 0%, 40%);
            --text-color-heading: hsl(0, 0%, 30%);
            --link-color: hsl(168, 52%, 39%);
            --link-hover-color: hsl(0, 0%, 0%);
            --background-color: hsl(0, 0%, 88%);
        }

        /* RESET ----------------------------------------------- */
        html, body, h1, p, ul, li, strong {
            font-size: inherit;
            letter-spacing: inherit;
            padding: 0;
            margin: 0;
            border-width: 0;
            box-sizing: border-box;
        }

        html {
            font-size: 100%;
        }

        body {
            line-height: 1.75;
        }

        /* LAYOUT & TYPO & COLOR ------------------------------- */
        body {
            font-family: var(--font-family);
            padding: 1.5rem 2rem 10rem 2rem;
            color: var(--text-color);
            background-color: var(--background-color);
        }

        h1 {
            font-size: 200%;
            font-weight: 100;
            letter-spacing: .7rem;
            color: var(--text-color-heading);
            margin-bottom: .5rem;
        }

        p {
            margin-bottom: .5rem;
        }

        ul {
            list-style: square;
            list-style-position: inside;
        }

        a {
            cursor: pointer;
        }

        a:link, a:visited {
            text-decoration-line: underline;
            text-decoration-style: dotted;
            color: var(--link-color);
        }

        a:hover, a:focus, a:active {
            text-decoration-style: solid;
            color: var(--link-hover-color);
        }
    </style>
</head>
<body>
    <h1>Cool Webradios</h1>
    <p>
        Tune-in: <a href="./cool-webradios.m3u">cool-webradios.m3u</a><br>
        Source: <a href="https://github.com/etrusci-org/cool-webradios">GitHub</a>
    </p>
    <ul>{list}</ul>
</body>
</html>
