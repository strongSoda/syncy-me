# flask app setup and home api route

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# render the index.html file
@app.route('/<id>')
def index(id):
    # render the index.html file
    # return send_file('index.html')

    # javascript api call
    # fetch(`https://L7PFECEWC3.algolia.net/1/indexes/syncy/${id}`, {
    #     method: 'GET',
    #     headers: {
    #         'X-Algolia-API-Key': 'a953f96171e71bef23ebd1760c7dea10',
    #         'X-Algolia-Application-Id': 'L7PFECEWC3',
    #     }
    # })

    # convert the above javascript api call to python code
    import requests
    url = f'https://L7PFECEWC3.algolia.net/1/indexes/syncy/{id}'
    headers = {
        'X-Algolia-API-Key': 'a953f96171e71bef23ebd1760c7dea10',
        'X-Algolia-Application-Id': 'L7PFECEWC3',
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print('here', data)

    # return the response from the above api call


    # send multiline html string
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- favicon -->
    <link rel="icon" href="https://i.imgur.com/P7kIQEm.png" type="image/x-icon">

    <title>''' + data["name"] + ''' | Book a call on Syncy</title>
    <!-- meta tags empty -->
    <meta name="description" content="
    ''' + data["bio"] + '''
    ">
    <meta name="keywords" content="
    ''' + ','.join(data["categories"]) + '''
    ">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- og meta tags empty -->
    <meta property="og:title" content="''' + data["name"] + ''' | Book a call on Syncy">
    <meta property="og:description" content="
    ''' + data["bio"] + '''
    ">
    <meta property="og:image" content="
    ''' + data["profile_image_url"] + '''
    ">

    <!-- twitter meta tags empty -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="''' + data["name"] + ''' | Book a call on Syncy">
    <meta name="twitter:description" content="
    ''' + data["bio"] + '''
    ">
    <meta name="twitter:image" content="">
    <meta name="twitter:image" content="
    ''' + data["profile_image_url"] + '''
    ">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            /* checks linear gradient background*/
            font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            text-align: center;            
        }
        .profile {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 0 auto;
            width: 100%;
            max-width: 600px;
            padding: 1rem;
            

        }
        .linkedin-img {
            width: 1rem !important;
            /* border-radius: 50%; */
        }
        .profile-image img {
            width: 100%;
            max-width: 200px;
            border-radius: 100%;
            margin-bottom: 1rem;
        }
        .profile-location {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            margin-bottom: 1rem;

            color: gray;
        }
        .profile-categories-list {
            list-style: none;
        }
        .profile-categories-list li {
            display: inline-block;
            margin-right: 1rem;
            color: gray;

            background-color: #efeffd;
            border-radius: 4px;
            color: #41415a;
            font-size: 13px;
            font-weight: 500;
            letter-spacing: .5px;
            line-height: 16px;
            margin-top: 16px;
            padding: 2px 6px;
        }
        .profile-categories-list li::before {
            content: "#";
            /* margin-right: 1rem; */
        }
        .profile-categories-list li:last-child {
            margin-right: 0;
        }
        .book-call {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            margin-bottom: 1rem;
        }
        .book-call button {
            background-color: #4d68eb;
            color: white;
            border: none;
            border-radius: 5px;
            padding: .6rem  1rem;
            font-size: 1rem;
            cursor: pointer;

            border-radius: 40px;
            box-sizing: content-box;
            color: #fff;
            display: inline-block;
            font-size: 15px;
            font-weight: 600;
            letter-spacing: .6px;
            line-height: 24px;
            padding: 4px 24px;
            text-decoration: none;
            white-space: nowrap;
        }
        .book-call button:hover {
            background-color: #3b4eb8;
        }
        .profile-name {
            font-size: 40px;
            font-weight: 600;
            letter-spacing: .8px;
            line-height: 48px;
            text-transform: capitalize;
            /* font-size: 1.5rem; */
            /* font-weight: 600; */
            margin-bottom: 1rem;
            margin-top: 1rem;
        }
        .profile-bio {
            margin-bottom: 1rem;
            font-size: 18px;
            color: #565674;
        }
        .footer {
            width: 100vw;
            margin-top: 1rem;
            color: gray;
            background-color: #f9faff;

            /* fixed at bottom */
            position: fixed;
            bottom: 0;

            /* padding */
            padding: 1rem;
        }
        .footer a {
            color: #41415A;
        }
    </style>
</head>
<body>
    <!-- profile  with name, image, bio -->
    <div class="profile">
        <div class="profile-image">
            <img src="" alt="profile image">
        </div>
        <div class="profile-links">
            <a class="linkedin-url" target="_blank" rel="noopener noreferrer">
                <img class="linkedin-img" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="linkedin">
            </a>
        </div>
        <div class="profile-info">
            <h1 class="profile-name"></h1>
            <!-- book call button fixed bottom position -->
            <div class="book-call">
                <button>Book a call with me</button>
            </div>
            <p class="profile-bio"></p>
        </div>
        <div class="profile-location">
            <p>
                <span class="profile-city"></span>, <span class="profile-country"></span></p>
        </div>
        <!-- categories -->
        <div class="profile-categories">
            <h4>Talks about</h4>
            <ul class="profile-categories-list">
            </ul>
        </div>

        <!-- footer powered by Syncy.net -->
        <div class="footer">
            <p>Powered by <a href="https://syncy.net" rel="noopener noreferrer">Syncy.net</a></p>
        </div>
    </div>

    <script>
        // get id from url
        const id = window.location.href.split('/').pop();
        console.log(id);
        // fetch profile data from algolia
        fetch(`https://L7PFECEWC3.algolia.net/1/indexes/syncy/${id}`, {
            method: 'GET',
            headers: {
                'X-Algolia-API-Key': 'a953f96171e71bef23ebd1760c7dea10',
                'X-Algolia-Application-Id': 'L7PFECEWC3',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // set profile data
            document.querySelector('.profile-name').textContent = data.name;
            document.querySelector('.profile-bio').textContent = data.bio;
            document.querySelector('.profile-image img').src = data.profile_image_url;
            document.querySelector('.linkedin-url').href = data.linkedin_url;
            document.querySelector('.profile-city').textContent = data.city;
            document.querySelector('.profile-country').textContent = data.country;
            // set categories
            const categories = data.categories;
            const categoriesList = document.querySelector('.profile-categories-list');
            categories.forEach(category => {
                const categoryItem = document.createElement('li');
                categoryItem.textContent = category;
                categoriesList.appendChild(categoryItem);
            });

        })
        .catch((error) => {
            console.error('Error:', error);
        });

        // book call button
        const bookCallButton = document.querySelector('.book-call button');
        bookCallButton.addEventListener('click', () => {
            bookCall(id)
        })


        // javascript code post request to / create - checkout - session
        const createCheckoutSession = async (profile_image_url, linkedin_url, name, bio, city, country, calendly_url, email, user_id, tags) => {
            const payload = {
                profile_image_url,
                linkedin_url,
                name,
                bio,
                city,
                country,
                calendly_url,
                email,
                user_id,
                tags: tags.join(', ')
            }
            console.log(payload);
            // const response = await fetch("http://127.0.0.1:5000/create-checkout-session", {
            const response = await fetch("https://syncy-backend.onrender.com/create-checkout-session", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            });
            console.log(response);
            const responseData = await response.json();
            console.log(responseData.data.url);
            location.href = responseData.data.url;
        };

        // wait until dom is ready
        const bookCall = async (id) => {
            console.log('booking clicked', id);

            document.querySelector('.book-call button').textContent = 'Loading...';

            // get the data by id from algolia v4
            const response = await fetch(`https://L7PFECEWC3-dsn.algolia.net/1/indexes/syncy/${id}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "X-Algolia-API-Key": "a953f96171e71bef23ebd1760c7dea10",
                    "X-Algolia-Application-Id": "L7PFECEWC3"
                },
            });
            const data = await response.json();
            console.log(data);
            const res = await createCheckoutSession(data.profile_image_url, data.linkedin_url, data.name, data.bio, data.city, data.country, data.calendly_url, data.email, data.objectID, data.categories);
        };
  
    </script>
</body>
</html>
        '''


if __name__ == '__main__':
    app.run(debug=True)


