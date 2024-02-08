"""Model Renderer"""
import os

directory = os.getcwd()
directory = directory.removesuffix('tools')
modelsDIR = directory + '/assets/models/'
missilesDIR = directory + '/assets/models/missiles/'
targetsDIR = directory + '/assets/models/targets/'
launchersDIR = directory + '/assets/models/launchers/'
decalsDIR = directory + '/assets/display/decals/'
shadersDIR = directory + '/assets/display/shading/'
surfacesDIR = directory + '/assets/display/surfaces/'
texturesDIR = directory + '/assets/display/textures/'

print('Models:', modelsDIR)
print('Missiles:', missilesDIR)
print('Targets:', targetsDIR)
print('Launchers:', launchersDIR)
print('Decals:', decalsDIR)
print('Shaders:', shadersDIR)
print('Surfaces:', surfacesDIR)
print('Textures:', texturesDIR)
