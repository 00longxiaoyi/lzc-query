rm -rf ./content/*
cd ./ui
pnpm run build
cp -r ./dist/ ../content/
