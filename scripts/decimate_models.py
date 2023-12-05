import bpy
import time
import os

decimate_ratio = 0.05
min_number_of_faces = 5000
path_to_model_directory = "your_model_directory_path"


class decimateModifier():

    def __init__(self, model_type, model_dir) -> None:
        self.object_count = 0
        self.objects = []
        self.model_path = []
        self.start_time = time.time()
        self.object_edges = 0
        self.object_vertices = 0
        self.object_polygons = 0
        self.model_count = 0
        self.findModels(model_type, model_dir)

    def clearScene(self):
        self.object_list = bpy.data.objects
        for obj in self.object_list:
            self.object_list.remove(obj, do_unlink=True)

    def log(self, msg):
        s = round(time.time() - self.start_time, 2)
        print("{}s | {}".format(s, msg))

    def importModel(self, path):
        bpy.ops.wm.collada_import(filepath=path)
        self.log("Collada IMPORT Complete")

    def getObjects(self):
        for obj in self.object_list:
            if (obj.type == "MESH"):
                self.objects.append(obj.name)
                self.object_count += 1
        self.log("Object count: {}".format(self.object_count))
        # self.log("Objects: {}".format(list(self.objects)))
        if (self.object_count != 0):
            self.active_object = bpy.data.objects[self.objects[-1]]
            bpy.context.view_layer.objects.active = self.active_object

    def joinObjects(self):
        if self.object_count > 1:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.join()

    def get_stats(self):
        self.object_edges = len(self.active_object.data.edges)
        self.object_vertices = len(self.active_object.data.vertices)
        self.object_polygons = len(self.active_object.data.polygons)
        self.log("No of Objects: {}, No of Edges: {}, No of Vertices: {}, No of Polygons: {}".format(self.object_count,
                                                                                                     self.object_edges, self.object_vertices, self.object_polygons))

    def applyDecimateModifier(self):
        if (self.object_polygons > min_number_of_faces):
            self.modifier = self.active_object.modifiers.new(
                "DecimateModifier", 'DECIMATE')
            self.modifier.ratio = decimate_ratio
            self.modifier.use_collapse_triangulate = True
            bpy.ops.object.modifier_apply(modifier="DecimateModifier")

    def exportModel(self, path):
        bpy.ops.wm.collada_export(
            filepath=path)
        self.log("Collada EXPORT Complete")

    def findModels(self, model_type, model_path):
        for root, dir, files in os.walk(model_path):
            for file in files:
                if file.endswith(model_type):
                    self.model_count += 1
                    self.model_path.append(os.path.join(root, file))
        # self.log(list(self.model_path))
        self.log("Total models to decimate in directory: {}".format(
            self.model_count))

    def decimateModel(self):
        self.getObjects()
        self.joinObjects()
        self.get_stats()
        self.applyDecimateModifier()
        self.get_stats()


if __name__ == "__main__":
    decimateMod = decimateModifier(".dae", path_to_model_directory)
    for model in range(len(decimateMod.model_path)):
        decimateMod.log("Model Number: {}".format(model))
        decimateMod.clearScene()
        decimateMod.importModel(decimateMod.model_path[model])
        decimateMod.decimateModel()
        decimateMod.exportModel(decimateMod.model_path[model])
