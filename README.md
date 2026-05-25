


## Technical Takeaway: How to Deploy on AWS EC2: Elastic Compute Cloud

### PART 0: Code Setup
1. Since this tutorial will makes both the frontend (Next.JS) and backend (FastAPI) sharing the same base URL, the following modifications is suggested on frontend:
```ts
const apiEndpoint = process.env.NEXT_PUBLIC_BACKEND_URL ?? ""
```
* Therefore, in the deployed instance, the environment key `NEXT_PUBLIC_BACKEND_URL` needs not to be set.
* Meanwhile, in local development, by setting it, it still allows the frontend to access the backend.

### PART 1: Launch EC2 Instance
1. Configure:
    * Name: `toki_pitcher`
    * AMI (Amazon Machine Image): Ubuntu LTS
    * Instance type: t2.small (free tier)
        * Recommended because of having 2GB RAM, t2.micro only has 1GB RAM and is not sufficient for this app.
    * Key pair: Create and download the key as `toki_pitcher_key.pem`

2. Under Network Settings --> Edit to add these inbound rules:
    | Type | Port | Source | Purpose |
    | ---- | ---- | ------ | ------- |
    | SSH | 22 | My IP | To connect local device's terminal with the EC2 Instance's terminal |
    | HTTP | 80 | Anywhere | To connect to the rendered application |

3. Launch Instance
    

### PART 2: SSH (Secure Shell) Into The Server
```bash
# On your laptop, restrict key permissions
chmod 400 my-app-key.pem

# SSH in
ssh -i my-app-key.pem ubuntu@<your-ec2-public-ip>
```

* `chmod` stands for change mode — it controls who can read/write/execute a file on Linux/Mac.
    * The 400 means:
        * 4 = owner can read
        * 0 = group cannot do anything
        * 0 = others cannot do anything

* `-i` stands for identity file — it tells SSH which private key file to use to authenticate


### PART 3: Install Dependencies
```bash
# Update server
sudo apt update && sudo apt upgrade -y

# Install Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install Python
sudo apt install -y python3

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload shell so uv is available
source $HOME/.local/bin/env

# Install Git
sudo apt install -y git

# Install Nginx
sudo apt install -y nginx

# Install PM2
sudo npm install -g pm2

# Verify installations
node -v
python3 --version
uv --version
nginx -v
```

### Part 4: Clone Github Repository
```bash
git clone https://github.com/wengti/toki-pitcher.git
cd toki-pitcher
```

### Part 5: Setup FastAPI Backend
1. Install dependencies for the backend and create `.env` file to store environment variables.
```bash
cd backend

# uv will automatically read your pyproject.toml
# and create a virtual environment + install dependencies
uv sync

# Create .env file
nano .env
```

2. Hint on how to save and exit nano
    * Ctrl + X to exit
    * Y to confirm save
    * Enter to confirm the filename

3. Initialize the backend instance by exposing port 8000
```bash
pm2 start "uv run uvicorn main:app --host 0.0.0.0 --port 8000" --name fastapi
```

### Part 6: Setup Next.JS Frontend
1. Create `.env` file and store the frontend's environment variables.
```bash
cd ../frontend

# Create .env
nano .env
```

2. Install, build and start the frontend instance
```bash
npm install
npm run build
pm2 start "npm start" --name nextjs
```

### Part 7: Save PM2 processes
```bash
# Save process list so it survives reboots
pm2 save

# Generate startup script
pm2 startup

# Copy and run the command it outputs
```

### Part 8: Configure Nginx
When a user visits your site, NGINX intercepts the request, forwards it to the appropriate frontend/backend, and returns the result, masking the identity of your internal network.

1. Create the config file to help Nginx decides how to reroute
```bash
sudo nano /etc/nginx/sites-available/toki-pitcher
```

2. Paste the following config:
server {
    listen 80;
    server_name <your-ec2-public-ip>;

    location / {
        proxy_pass http://localhost:3000;
    }

    location /api/ {
        proxy_pass http://localhost:8000;
    }
}

3. Enable the config
```bash
# Enable your site
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/

# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Test config is valid
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx

# Enable Nginx on reboot
sudo systemctl enable nginx
```



### PART 9: Verify Everything Works
```bash
# Check Nginx is running
sudo systemctl status nginx

# Check PM2 processes
pm2 status

# Check backend logs if something is wrong
pm2 logs fastapi

# Check frontend logs if something is wrong
pm2 logs nextjs
```
* Visit the site at `http://<your-ec2-public-ip>`

### PART 10: Deploy Update
```bash
cd your-repo
git pull

# Restart backend
cd backend
uv sync          # picks up any new dependencies from pyproject.toml
pm2 restart fastapi

# Rebuild and restart frontend
cd ../frontend
npm install      # in case dependencies changed
npm run build
pm2 restart nextjs
```

### PART 11: What to pay attention to after stopping and restarting an EC2 instance
1. The public IP address will change.


## Technical Takeaway: Generating Type Schema from Supabase

### TypeScript
1. Follow the following guide is suffice
    * https://supabase.com/docs/guides/api/rest/generating-types

### Python
1. Following the following guide for the most part, except for the final step:
    * https://supabase.com/docs/guides/api/rest/generating-python-types

2. Final Step
```bash
npx supabase gen types --lang=python --db-url "<session-pooler-connection-string>" --schema public > model/supabase_model.py
```