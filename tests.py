# -*- coding: utf-8 -*-
import unittest2 as unittest
import os
import tempfile
import shutil

from scripttest import TestFileEnvironment


class BaseTemplateTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree,
                self.tempdir)

        # docs httpcripttest//pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(
            os.path.join(self.tempdir,
                    'test-output'),
            ignore_hidden=False,
        )

    def create_template(self):
        """Run mr.bob to create your template."""
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
            'project': self.project,
        }
        return self.env.run(
            '%(dir)s/bin/mrbob -O %(project)s --config '
            '%(dir)s/test_answers.ini %(dir)s/bobtemplates/%(template)s'
            % options)


class PloneTemplateTest(BaseTemplateTest):
    """Tests for the `plone` template."""
    template = 'plone'
    project = 'collective.foo'

    def test_plone_template(self):
        """Test the `plone` template.

        Generate a project from a template and test which files were created.
        """
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            ['collective.foo',
                'collective.foo/src/collective/foo/profiles/uninstall',
                'collective.foo/src/collective/foo/tests/test_setup.py',
                'collective.foo/.travis.yml',
                'collective.foo/src/collective/foo/profile.py',
                'collective.foo/src/collective/foo/locales',
                'collective.foo/docs',
                'collective.foo/src/collective/foo/tests',
                'collective.foo/src/collective/foo/Extensions',
                'collective.foo/src/collective/foo/profiles',
                'collective.foo/src/collective/foo/profiles/testing/properties.xml',
                'collective.foo/src/collective/foo/Extensions/__init__.py',
                'collective.foo/src',
                'collective.foo/src/collective/foo/__init__.py',
                'collective.foo/src/collective/foo/browser',
                'collective.foo/README.rst',
                'collective.foo/src/collective/foo/profiles/default',
                'collective.foo/src/collective/foo/browser/static/.gitkeep',
                'collective.foo/src/collective/foo/testing.zcml',
                'collective.foo/src/collective/foo/profiles/testing',
                'collective.foo/src/collective',
                'collective.foo/src/collective/foo/Extensions/install.py',
                'collective.foo/buildout.cfg',
                'collective.foo/src/collective/foo/setuphandlers.py',
                'collective.foo/src/collective/foo/profiles/uninstall/browserlayer.xml',
                'collective.foo/src/collective/__init__.py',
                'collective.foo/src/collective/foo/tests/__init__.py',
                'collective.foo/docs/LICENSE.rst',
                'collective.foo/src/collective/foo/tests/robot/test_example.robot',
                'collective.foo/src/collective/foo/profiles/default/browserlayer.xml',
                'collective.foo/src/collective/foo/profiles/testing/collective.foo.txt',
                'collective.foo/src/collective/foo/tests/robot',
                'collective.foo/src/collective/foo/locales/collective.foo.pot',
                'collective.foo/src/collective/foo/browser/configure.zcml',
                'collective.foo/src/collective/foo/tests/test_robot.py',
                'collective.foo/setup.py',
                'collective.foo/CHANGES.rst',
                'collective.foo/src/collective/foo',
                'collective.foo/src/collective/foo/interfaces.py',
                'collective.foo/src/collective/foo/browser/static',
                'collective.foo/src/collective/foo/profiles/default/metadata.xml',
                'collective.foo/MANIFEST.in',
                'collective.foo/src/collective/foo/profiles/testing/metadata.xml',
                'collective.foo/src/collective/foo/configure.zcml',
                'collective.foo/src/collective/foo/testing.py',
                'collective.foo/.gitignore',
                'collective.foo/src/collective/foo/browser/__init__.py',
                'collective.foo/Makefile']

        )
