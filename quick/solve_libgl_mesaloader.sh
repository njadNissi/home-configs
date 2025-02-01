conda_path="/data/$USER/anaconda3"
read -p "Path to miniconda or anaconda3 folder: <<$conda_path>>. [y|n]: " choice
if [ "$choice" != "y" ]; then
	read -p "Enter path to miniconda or anaconda3 folder: "	conda_path
fi
read -p "Enter the conda environment name: " envname

cd "$conda_path/envs/$envname/lib"
echo "===> Entered in: $PWD"

mkdir backup  # Create a new folder to keep the original libstdc++
mv libstd* backup  # Put all libstdc++ files into the folder, including soft links
echo "===> Created a backup folder for .so files"

cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6  ./ 
echo "===> Copy the c++ dynamic link library of the system here"

ln -s libstdc++.so.6 libstdc++.so
ln -s libstdc++.so.6 libstdc++.so.6.0.19
echo "===> Creating symlink to libstdc.so.6"
